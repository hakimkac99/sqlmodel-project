from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import create_db_and_tables

from .api.api import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await create_db_and_tables()
    yield
    # shutdown
    # ...


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
