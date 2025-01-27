from typing import Optional

from sqlmodel import SQLModel, Field


class Faculty(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    student_id: Optional[int] = Field(default=None, foreign_key="student.id")
    teacher_id: Optional[int] = Field(default=None, foreign_key="teacher.id")