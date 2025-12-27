from sqlalchemy.orm import Session
import uuid

from app.db import engine, Base, SessionLocal
from app.models import Student, HealthLog
from app.schemas import (
    StudentCreate,
    StudentResponse,
    HealthLogCreate,
    AnalyzeRequest,
    AnalyzeResponse,
    GeneralProfile,
)

from app.health_engine import (
    analyze_student_health,
    analyze_sleep_patterns,
    analyze_nutrient_deficiency,
    generate_personalized_student_advice,
    generate_budget_meal_plan,
    analyze_mess_food,
)

from app.general_engine import (
    generate_diet,
    generate_workout,
    generate_health_summary,
    mental_wellness_support,
    protein_planning,
    what_if_simulation,
)
app = FastAPI(title="AI Health Backend")

# ---------------- CORS (AFTER APP) ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- DATABASE ----------------

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------- ROOT ----------------

@app.get("/")
def root():
    return {"status": "Backend running"}

# ---------------- STUDENT CREATE ----------------

@app.post("/student/create", response_model=StudentResponse)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    student_id = str(uuid.uuid4())

    student = Student(
        id=student_id,
        age=data.age,
        height=data.height,
        weight=data.weight,
        budget=data.budget,
        bmi=data.bmi,
    )

    db.add(student)
    db.commit()

    return {"student_id": student_id}

# ---------------- STUDENT LOG ----------------

@app.post("/student/log")
def add_health_log(data: HealthLogCreate, db: Session = Depends(get_db)):
    log = HealthLog(
        student_id=data.student_id,
        date=data.date,
        sleep_hours=data.sleep_hours,
        junk_food=data.junk_food,
        energy=data.energy,
    )

    db.add(log)
    db.commit()

    return {"message": "Health log saved"}

# ---------------- STUDENT ANALYZE ----------------

@app.post("/student/analyze", response_model=AnalyzeResponse)
def analyze_student(data: AnalyzeRequest, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == data.student_id).first()
    if not student:
        return {"analysis": "Student not found"}

    logs = (
        db.query(HealthLog)
        .filter(HealthLog.student_id == data.student_id)
        .order_by(HealthLog.date.desc())
        .limit(5)
        .all()
    )

    profile = {
        "age": student.age,
        "height": student.height,
        "weight": student.weight,
        "budget": student.budget,
        "bmi": student.bmi,
    }

    log_data = [
        {
            "date": log.date,
            "sleep_hours": log.sleep_hours,
            "junk_food": log.junk_food,
            "energy": log.energy,
        }
        for log in logs
    ]

    return {"analysis": analyze_student_health(profile, log_data)}

# ---------------- GENERAL MODE ----------------

@app.post("/general/diet")
def general_diet(data: GeneralProfile):
    return {"diet_plan": generate_diet(data.dict())}

@app.post("/general/workout")
def general_workout(data: GeneralProfile):
    return {"workout_plan": generate_workout(data.dict())}

@app.post("/general/summary")
def general_summary(data: GeneralProfile):
    return {"summary": generate_health_summary(data.dict())}

@app.post("/general/mental")
def general_mental(data: GeneralProfile):
    return {"mental_support": mental_wellness_support(data.dict())}

@app.post("/general/protein")
def general_protein(data: GeneralProfile):
    return {"protein_plan": protein_planning(data.dict())}

@app.post("/general/what-if")
def general_what_if(data: GeneralProfile):
    return {"simulation": what_if_simulation(data.dict())}
