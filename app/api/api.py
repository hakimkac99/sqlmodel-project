from fastapi import APIRouter

from .endpoints import heros

api_router = APIRouter()
api_router.include_router(heros.router, tags=["heros"])
