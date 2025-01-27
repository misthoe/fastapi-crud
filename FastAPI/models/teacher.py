from sqlmodel import SQLModel, Field


class Teacher(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    last_name: str
    specialty: str
    age: int | None = None
    salary: float | None = None