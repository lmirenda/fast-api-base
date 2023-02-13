import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture(scope="session")
def client():
    with TestClient(app) as _client:
        yield _client


def test_async_route(client: TestClient) -> None:
    response = client.get("/sync/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a synchronous route"}
