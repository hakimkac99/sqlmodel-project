from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app import crud
from app.db import get_session
from app.models.hero import HeroRead
from app.models.team import TeamCreate, TeamRead, TeamReadWithHeroes, TeamUpdate

TeamReadWithHeroes.update_forward_refs(HeroRead=HeroRead)

router = APIRouter()


@router.post("/teams/", response_model=TeamRead)
async def create_team(*, session: Session = Depends(get_session), team: TeamCreate):
    db_team = await crud.team.create(session=session, obj_in=team)
    return db_team


@router.get("/teams/", response_model=List[TeamReadWithHeroes])
async def read_teams(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    teams = await crud.team.read_multi(session=session, offset=offset, limit=limit)
    return teams


@router.get("/teams/{team_id}", response_model=TeamReadWithHeroes)
async def read_team(*, team_id: int, session: Session = Depends(get_session)):
    team = await crud.team.read_by_id(session=session, id=team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.patch("/teams/{team_id}", response_model=TeamRead)
async def update_team(
    *,
    session: Session = Depends(get_session),
    team_id: int,
    team: TeamUpdate,
):
    db_team = await crud.team.read_by_id(session=session, id=team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    updated_team = await crud.hero.update(session=session, db_obj=db_team, obj_in=team)
    return updated_team


@router.delete("/teams/{team_id}")
async def delete_team(*, session: Session = Depends(get_session), team_id: int):
    db_team = await crud.team.read_by_id(session=session, id=team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    await crud.team.delete(session=session, id=team_id)
    return {"ok": True}
