from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from fastapi_controllers import Controller, get, delete, put, post

from db import get_session
from models.student import Student


class StudentController(Controller):

    @get("/students")
    async def get_all_students(self, session: Session = Depends(get_session)) -> list[Student]:
        students = session.exec(select(Student)).all()
        student_list = [s for s in students]
        return student_list

    @get("/student/{student_id}")
    async def get_student_by_id(self, student_id: int, session: Session = Depends(get_session)) -> Student:
        query = select(Student).where(Student.id == student_id)
        student = session.exec(query).first()
        return student

    @delete("/student/{student_id}")
    async def delete_student_by_id(self, student_id: int, session: Session = Depends(get_session)) -> str:
        statement = select(Student).where(Student.id == student_id)
        student = session.exec(statement).first()
        if student:
            session.delete(student)
            session.commit()
            return f"Deleted Student with id: {student_id}"
        else:
            raise HTTPException(status_code=404, detail=f"Student with id {student_id} not found")

    @put("/student/{student_id}")
    def update_student(self, student_to_update: Student, session: Session = Depends(get_session)):
        statement = select(Student).where(Student.id == student_to_update.id)
        student = session.exec(statement).first()
        if student:
            student.name = student_to_update.name
            student.last_name = student_to_update.last_name
            student.age = student_to_update.age
            student.major = student_to_update.major
            session.add(student)
            session.commit()
            return student
        else:
            raise HTTPException(status_code=404, detail=f"Student with id {student_to_update.id} not found")

    @post("/student")
    async def create_student(self, student: Student, session: Session = Depends(get_session)) -> Student:
        student = Student(name=student.name, last_name=student.last_name, major=student.major, age=student.age)
        session.add(student)
        session.commit()
        session.refresh(student)
        return student
