from typing import Generator, Any

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine, Session

from db import get_session
from main import app

test_engine = create_engine("sqlite:///test.db")
SQLModel.metadata.create_all(test_engine)


def override_get_session() -> Generator[Session, Any, None]:
    session = Session(test_engine)
    try:
        yield session
    finally:
        session.close()


app.dependency_overrides[get_session] = override_get_session
client = TestClient(app)


@pytest.fixture
def test_db() -> Generator[Any, Any, None]:
    SQLModel.metadata.create_all(test_engine)
    yield
    SQLModel.metadata.drop_all(test_engine)
