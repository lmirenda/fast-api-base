import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
from sqlmodel import Session

from src.models import Hero


@pytest.fixture
def anyio_backend():
    return "asyncio"


def test_create_hero(client: TestClient):
    response = client.post("api/v1/heroes/", json={"name": "Deadpool", "secret_name": "Dave Wilson"})
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Deadpool"
    assert data["secret_name"] == "Dave Wilson"
    assert data["age"] is None
    assert data["id"] is not None


def test_get_hero_from_db(session: Session):
    hero = Hero(name="Deadpool", secret_name="Dave Wilson")
    hero_db = Hero.from_orm(hero)
    session.add(hero_db)
    session.commit()
    hero_db_found = session.query(Hero).filter(Hero.name == "Deadpool").first()
    assert hero_db_found.name == "Deadpool"
    assert hero_db_found.secret_name == "Dave Wilson"
    assert hero_db_found.age is None


def test_get_hero_from_api(session: Session, client: TestClient):
    hero = Hero(name="Deadpool", secret_name="Dave Wilson")
    hero_db = Hero.from_orm(hero)
    session.add(hero_db)
    session.commit()
    response = client.get("api/v1/heroes/Deadpool")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Deadpool"
    assert data["secret_name"] == "Dave Wilson"
    assert data["age"] is None


@pytest.mark.anyio
async def test_main_route(async_client: AsyncClient) -> None:
    response = await async_client.get("/api/v1/heroes")
    assert response.status_code == 307


def test_hero_not_found(client: TestClient):
    response = client.get("api/v1/heroes/Deadpool")
    assert response.status_code == 404
    assert response.json() == {"detail": "Hero not found"}


def test_hero_not_created_when_name_not_provided(client: TestClient):
    response = client.post("api/v1/heroes/", json={"secret_name": "Dave Wilson"})
    expected_response = {"detail": [{"loc": ["body", "name"], "msg": "field required", "type": "value_error.missing"}]}
    assert response.status_code == 422
    assert response.json() == expected_response
