from fastapi import Depends
from fastapi_controllers import Controller, get, delete, put, post
from sqlmodel import Session

from crud.teacher import create_teacher, get_all_teachers, get_teacher_by_id, delete_teacher_by_id, update_teacher
from db import get_session
from models.teacher import Teacher


class TeacherController(Controller):

    @post("/teacher")
    async def create_teacher(self, teacher: Teacher, session: Session = Depends(get_session)) -> Teacher:
        return await create_teacher(teacher, session)

    @get("/teachers")
    async def get_all_teachers(self, session: Session = Depends(get_session)) -> list[Teacher]:
        return await get_all_teachers(session)

    @get("/teacher/{teacher_id}")
    async def get_teacher_by_id(self, teacher_id: int, session: Session = Depends(get_session)) -> Teacher:
        return await get_teacher_by_id(teacher_id, session)

    @delete("/teacher/{teacher_id}")
    async def delete_teacher_by_id(self, teacher_id: int, session: Session = Depends(get_session)) -> str:
        return await delete_teacher_by_id(teacher_id, session)

    @put("/teacher/{teacher_id}")
    async def update_teacher(self, teacher_to_update: Teacher, session: Session = Depends(get_session)) -> Teacher:
        return await update_teacher(teacher_to_update, session)
