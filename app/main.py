from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict to Vercel URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI, Depends
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

Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Health Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"status": "Backend running"}

# ---------------- STUDENT ----------------

@app.post("/student/create", response_model=StudentResponse)
def create_student(data: StudentCreate, db: Session = Depends(get_db)):
    student_id = str(uuid.uuid4())
    student = Student(id=student_id, **data.dict())
    db.add(student)
    db.commit()
    return {"student_id": student_id}


@app.post("/student/log")
def log_health(data: HealthLogCreate, db: Session = Depends(get_db)):
    db.add(HealthLog(**data.dict()))
    db.commit()
    return {"message": "Log saved"}


def fetch_student_context(student_id, db):
    student = db.query(Student).filter(Student.id == student_id).first()
    logs = (
        db.query(HealthLog)
        .filter(HealthLog.student_id == student_id)
        .order_by(HealthLog.date.desc())
        .limit(7)
        .all()
    )
    profile = {
        "age": student.age,
        "height": student.height,
        "weight": student.weight,
        "budget": student.budget,
        "bmi": student.bmi,
    }
    log_data = [log.__dict__ for log in logs]
    return student, profile, log_data


@app.post("/student/analyze", response_model=AnalyzeResponse)
def student_analysis(data: AnalyzeRequest, db: Session = Depends(get_db)):
    _, profile, logs = fetch_student_context(data.student_id, db)
    return {"analysis": analyze_student_health(profile, logs)}


@app.post("/student/sleep-analysis")
def sleep(data: AnalyzeRequest, db: Session = Depends(get_db)):
    _, profile, logs = fetch_student_context(data.student_id, db)
    return {"analysis": analyze_sleep_patterns(profile, logs)}


@app.post("/student/nutrient-risk")
def nutrients(data: AnalyzeRequest, db: Session = Depends(get_db)):
    _, profile, logs = fetch_student_context(data.student_id, db)
    return {"analysis": analyze_nutrient_deficiency(profile, logs)}


@app.post("/student/advice")
def advice(data: AnalyzeRequest, db: Session = Depends(get_db)):
    _, profile, logs = fetch_student_context(data.student_id, db)
    return {"analysis": generate_personalized_student_advice(profile, logs)}


@app.post("/student/mess-food")
def mess_food(data: AnalyzeRequest, db: Session = Depends(get_db)):
    _, profile, logs = fetch_student_context(data.student_id, db)
    return {"analysis": analyze_mess_food(profile, logs)}


@app.post("/student/budget-meal")
def budget_meal(data: AnalyzeRequest, db: Session = Depends(get_db)):
    _, profile, logs = fetch_student_context(data.student_id, db)
    return {"analysis": generate_budget_meal_plan(profile, logs)}

# ---------------- GENERAL ----------------

@app.post("/general/diet")
def diet(data: GeneralProfile):
    return {"diet_plan": generate_diet(data.dict())}

@app.post("/general/workout")
def workout(data: GeneralProfile):
    return {"workout_plan": generate_workout(data.dict())}

@app.post("/general/summary")
def summary(data: GeneralProfile):
    return {"summary": generate_health_summary(data.dict())}

@app.post("/general/mental")
def mental(data: GeneralProfile):
    return {"mental_support": mental_wellness_support(data.dict())}

@app.post("/general/protein")
def protein(data: GeneralProfile):
    return {"protein_plan": protein_planning(data.dict())}

@app.post("/general/what-if")
def what_if(data: GeneralProfile):
    return {"simulation": what_if_simulation(data.dict())}
