import pytest_asyncio
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import Session, SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel.pool import StaticPool

from app.db import get_session
from app.main import app


@pytest_asyncio.fixture(name="session")
async def session_fixture():
    engine = create_async_engine("sqlite+aiosqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    async with engine.begin() as conn:
        # await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)

        async_session = sessionmaker(
            engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )
        async with async_session() as session:
            yield session


@pytest_asyncio.fixture(name="client")
async def client_fixture(session: Session):
    async def get_session_override():
        return session

    app.dependency_overrides[get_session] = get_session_override
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
        app.dependency_overrides.clear()
