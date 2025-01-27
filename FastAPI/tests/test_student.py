from fastapi import Depends
from fastapi.testclient import TestClient
from sqlmodel import Session

from FastAPI.main import app
from db import get_session, SessionLocal
from models.student import Student

client = TestClient(app)


async def create_student(student: Student, session: Session = Depends(get_session)) -> Student:
    student = Student(name=student.name, last_name=student.last_name, major=student.major, age=student.age)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student

def test_create_student():

    response = client.post("/student/", json={"name": "John", "last_name": "Doe", "major": "math", "age": 30,
                                              "doctoral_candidate": "false"})
    assert response.status_code == 200
    assert response.json()["name"] == "John"


