from fastapi import Depends
from fastapi_controllers import Controller, get
from sqlmodel import Session, select

from db import get_session
from models.faculty import Faculty


class FacultyController(Controller):

    @get("/faculty")
    async def get_all_faculty(self, session: Session = Depends(get_session)) -> list[Faculty]:
        faculty = session.exec(select(Faculty)).all()
        faculty_list = [f for f in faculty]
        return faculty_list
