from pydantic import BaseModel
from typing import List

# ---------- STUDENT ----------

class StudentCreate(BaseModel):
    age: int
    height: float
    weight: float
    budget: str
    bmi: float


class StudentResponse(BaseModel):
    student_id: str


# ---------- HEALTH LOG ----------

class HealthLogCreate(BaseModel):
    student_id: str
    date: str
    sleep_hours: float
    junk_food: bool
    energy: int


# ---------- ANALYSIS ----------

class AnalyzeRequest(BaseModel):
    student_id: str


class AnalyzeResponse(BaseModel):
    analysis: str
# ---------- GENERAL FITNESS ----------

class GeneralProfile(BaseModel):
    name: str
    age: int
    height: float
    weight: float
    goal: str
    activity_level: int
    diet_type: str
