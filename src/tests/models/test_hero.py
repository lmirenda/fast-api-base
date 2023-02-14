from fastapi.testclient import TestClient
from sqlmodel import Session

from src.models import Hero


def test_create_hero(client: TestClient):
    response = client.post(
        "/heroes/", json={"name": "Deadpool", "secret_name": "Dave Wilson"}
    )
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
    hero_db = Hero.from_orm(hero)
    session.add(hero_db)
    session.commit()
    response = client.get("/heroes/Deadpool")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Deadpool"
    assert data["secret_name"] == "Dave Wilson"
    assert data["age"] is None
