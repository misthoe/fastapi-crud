from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine, SQLModel, Session

DATABASE_URL = 'sqlite:///db.sqllite'

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    SQLModel.metadata.create_all(bind=engine)


def get_session() -> Session:
    with Session(engine) as session:
        yield session
