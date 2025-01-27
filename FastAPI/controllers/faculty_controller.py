from fastapi import Depends
from fastapi_controllers import Controller, get
from sqlmodel import Session

from crud.faculty import get_all_faculty
from db import get_session
from models.faculty import Faculty


class FacultyController(Controller):

    @get("/faculty")
    async def get_all_faculty(self, session: Session = Depends(get_session)) -> list[Faculty]:
        return await get_all_faculty(session)
