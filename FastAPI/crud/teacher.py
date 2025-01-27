from fastapi import Depends, HTTPException
from sqlmodel import Session, select

from db import get_session
from models.teacher import Teacher


async def create_teacher(teacher: Teacher, session: Session = Depends(get_session)) -> Teacher:
    teacher = Teacher(name=teacher.name, last_name=teacher.last_name, specialty=teacher.specialty, age=teacher.age,
                      salary=teacher.salary)
    session.add(teacher)
    session.commit()
    session.refresh(teacher)
    return teacher


async def get_all_teachers(session: Session = Depends(get_session)) -> list[Teacher]:
    teachers = session.exec(select(Teacher)).all()
    teachers_list = [t for t in teachers]
    return teachers_list


async def get_teacher_by_id(teacher_id: int, session: Session = Depends(get_session)) -> Teacher:
    query = select(Teacher).where(Teacher.id == teacher_id)
    teacher = session.exec(query).first()
    return teacher

async def delete_teacher_by_id(teacher_id: int, session: Session = Depends(get_session)) -> str:
    statement = select(Teacher).where(Teacher.id == teacher_id)
    teacher = session.exec(statement).first()
    if teacher:
        session.delete(teacher)
        session.commit()
        return f"Deleted teacher with id: {teacher_id}"
    else:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher.id} not found")


def update_teacher(teacher_to_update: Teacher, session: Session = Depends(get_session)) -> Teacher:
    statement = select(Teacher).where(Teacher.id == teacher_to_update.id)
    teacher = session.exec(statement).first()
    if teacher:
        teacher.name = teacher_to_update.name
        teacher.last_name = teacher_to_update.last_name
        teacher.age = teacher_to_update.age
        teacher.salary = teacher_to_update.salary
        teacher.specialty = teacher_to_update.specialty
        session.add(teacher)
        session.commit()
        return teacher
    else:
        raise HTTPException(status_code=404, detail=f"Teacher with id {teacher.id} not found")
