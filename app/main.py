from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlmodel import SQLModel

from app import db

from .api.api import api_router
from .models import *


def create_db_and_tables():
    SQLModel.metadata.create_all(db.engine)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    create_db_and_tables()
    yield
    # shutdown
    # ...


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
