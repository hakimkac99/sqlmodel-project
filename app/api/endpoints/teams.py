from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app import crud
from app.db import get_session
from app.models.team import TeamCreate, TeamRead, TeamUpdate
from app.models.team_hero_ import TeamReadWithHeroes

router = APIRouter()


@router.post("/teams/", response_model=TeamRead)
def create_team(*, session: Session = Depends(get_session), team: TeamCreate):
    db_team = crud.team.create(session=session, obj_in=team)
    return db_team


@router.get("/teams/", response_model=List[TeamReadWithHeroes])
def read_teams(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    teams = crud.team.read_multi(session=session, offset=offset, limit=limit)
    return teams


@router.get("/teams/{team_id}", response_model=TeamReadWithHeroes)
def read_team(*, team_id: int, session: Session = Depends(get_session)):
    team = crud.team.read_by_id(session=session, id=team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team


@router.patch("/teams/{team_id}", response_model=TeamRead)
def update_team(
    *,
    session: Session = Depends(get_session),
    team_id: int,
    team: TeamUpdate,
):
    db_team = crud.team.read_by_id(session=session, id=team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    updated_team = crud.hero.update(session=session, db_obj=db_team, obj_in=team)
    return updated_team


@router.delete("/teams/{team_id}")
def delete_team(*, session: Session = Depends(get_session), team_id: int):
    db_team = crud.team.read_by_id(session=session, id=team_id)
    if not db_team:
        raise HTTPException(status_code=404, detail="Team not found")
    crud.team.delete(session=session, id=team_id)
    return {"ok": True}
