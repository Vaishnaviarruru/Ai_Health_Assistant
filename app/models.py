from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from app.db import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(String, primary_key=True, index=True)
    age = Column(Integer)
    height = Column(Float)
    weight = Column(Float)
    budget = Column(String)
    bmi = Column(Float)

class HealthLog(Base):
    __tablename__ = "health_logs"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, ForeignKey("students.id"))
    date = Column(String)
    sleep_hours = Column(Float)
    junk_food = Column(Boolean)
    energy = Column(Integer)
