from contextlib import asynccontextmanager
from typing import Dict

from fastapi import FastAPI

from controllers.student_controller import StudentController
from controllers.teacher_controller import TeacherController
from controllers.faculty_controller import FacultyController
from db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def landing_page() -> Dict:
    return {"message": "Hello!"}


app.include_router(StudentController().create_router())
app.include_router(TeacherController().create_router())
app.include_router(FacultyController().create_router())
