from fastapi import Depends
from sqlmodel import Session, select

from db import get_session
from models.faculty import Faculty


async def get_all_faculty(session: Session = Depends(get_session)) -> list[Faculty]:
    faculty = session.exec(select(Faculty)).all()
    faculty_list = [f for f in faculty]
    return faculty_list
