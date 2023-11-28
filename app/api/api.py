from fastapi import APIRouter

from .endpoints import heros, teams

api_router = APIRouter()
api_router.include_router(heros.router, tags=["heros"])
api_router.include_router(teams.router, tags=["teams"])
