from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app import crud
from app.db import get_session
from app.models.hero import HeroCreate, HeroRead, HeroUpdate

router = APIRouter()


@router.post("/heroes/", response_model=HeroRead)
def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = crud.hero.create(session=session, obj_in=hero)
    return db_hero


@router.get("/heroes/", response_model=List[HeroRead])
def read_heroes(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    heros = crud.hero.read_multi(session=session, offset=offset, limit=limit)
    return heros


@router.patch("/heroes/{hero_id}", response_model=HeroRead)
def update_hero(*, session: Session = Depends(get_session), hero_id: int, hero: HeroUpdate):
    db_hero = crud.hero.read_by_id(session=session, id=hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    updated_hero = crud.hero.update(session=session, db_obj=db_hero, obj_in=hero)
    return updated_hero


@router.delete("/heroes/{hero_id}")
def delete_hero(*, session: Session = Depends(get_session), hero_id: int):
    db_hero = crud.hero.read_by_id(session=session, id=hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    crud.hero.delete(session=session, id=hero_id)
    return {"ok": True}
