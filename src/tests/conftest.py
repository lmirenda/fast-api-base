from typing import AsyncIterator

import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlmodel import Session, create_engine, SQLModel
from sqlmodel.pool import StaticPool

from src.main import app, get_session


@pytest.fixture(name="session")
def session_fixture():
    """
    Fixture that creates an instance of the SQLAlchemy session.
    All tests are run on a flushed database instance.
    """
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    """Creates a new synchronous FastAPI test client that connects to the session test database."""
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture(name="async_client")
async def async_client_fixture(session: Session) -> AsyncIterator[AsyncClient]:
    """Creates a new asynchronous FastAPI test client that connects to the session test database."""
    def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override

    client = AsyncClient(app=app, base_url="http://test")
    yield client
    app.dependency_overrides.clear()
