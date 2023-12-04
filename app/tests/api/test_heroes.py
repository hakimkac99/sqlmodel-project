from fastapi.testclient import TestClient
from sqlmodel import Session

from app import crud
from app.models.hero import HeroCreate


def test_create_hero(client: TestClient):
    response = client.post("/heroes/", json={"name": "Hakim", "secret_name": "Kac", "age": 25})
    data = response.json()

    assert response.status_code == 200
    assert data["name"] == "Hakim"
    assert data["secret_name"] == "Kac"
    assert data["age"] == 25
    assert data["id"] is not None


def test_delete_hero(session: Session, client: TestClient):
    hero = crud.hero.create(session=session, obj_in=HeroCreate(name="Ghani", secret_name="Kac"))
    response = client.delete(f"/heroes/{hero.id}")
    assert response.status_code == 200
    herro_in_db = crud.hero.read_by_id(session=session, id=hero.id)
    assert herro_in_db is None
