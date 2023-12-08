from fastapi import APIRouter

from .endpoints import abilities, heros, teams

api_router = APIRouter()
api_router.include_router(heros.router, tags=["heros"])
api_router.include_router(teams.router, tags=["teams"])
api_router.include_router(abilities.router, tags=["abilities"])
