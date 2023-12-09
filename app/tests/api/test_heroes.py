import pytest
from httpx import AsyncClient
from sqlmodel.ext.asyncio.session import AsyncSession

from app import crud
from app.models.hero import HeroCreate


@pytest.mark.asyncio
async def test_create_hero(client: AsyncClient):
    response = await client.post("/heroes/", json={"first_name": "Hakim", "last_name": "Kacemi", "age": 24})
    data = response.json()

    assert response.status_code == 200
    assert data["first_name"] == "Hakim"
    assert data["last_name"] == "Kacemi"
    assert data["age"] == 24
    assert data["id"] is not None


@pytest.mark.asyncio
async def test_delete_hero(session: AsyncSession, client: AsyncClient):
    hero = await crud.hero.create(session=session, obj_in=HeroCreate(first_name="Ghani", last_name="Kacemi"))
    response = await client.delete(f"/heroes/{hero.id}")
    assert response.status_code == 200
    herro_in_db = await crud.hero.read_by_id(session=session, id=hero.id)
    assert herro_in_db is None
