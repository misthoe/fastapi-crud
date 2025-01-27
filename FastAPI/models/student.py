from sqlmodel import SQLModel, Field


class Student(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name: str
    major: str
    age: int | None = None
    doctoral_candidate: bool = False