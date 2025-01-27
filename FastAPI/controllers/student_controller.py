from fastapi import Depends
from fastapi_controllers import Controller, get, delete, put, post
from sqlmodel import Session

from crud.student import get_all_students, get_student_by_id, delete_student_by_id, update_student, create_student
from db import get_session
from models.student import Student


class StudentController(Controller):

    @get("/students")
    async def get_all_students(self, session: Session = Depends(get_session)) -> list[Student]:
        return await get_all_students(session)

    @get("/student/{student_id}")
    async def get_student_by_id(self, student_id: int, session: Session = Depends(get_session)) -> Student:
        return await get_student_by_id(student_id, session)

    @delete("/student/{student_id}")
    async def delete_student_by_id(self, student_id: int, session: Session = Depends(get_session)) -> str:
        return await delete_student_by_id(student_id, session)

    @put("/student/{student_id}")
    async def update_student(self, student_to_update: Student, session: Session = Depends(get_session)):
        await update_student(student_to_update, session)

    @post("/student")
    async def create_student(self, student: Student, session: Session = Depends(get_session)) -> Student:
        return await create_student(student, session)
