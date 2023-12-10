from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app import crud
from app.db import get_session
from app.models.hero import HeroCreate, HeroRead, HeroReadWithTeam, HeroUpdate
from app.models.link_models import (
    HeroAbilityBase,
    HeroAbilityCreateUpdate,
    HeroAbilityLink,
)
from app.models.team import TeamRead

HeroReadWithTeam.update_forward_refs(TeamRead=TeamRead)

router = APIRouter()


@router.post("/heroes/", response_model=HeroRead)
async def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = await crud.hero.create(session=session, obj_in=hero)
    return db_hero


@router.get("/heroes/", response_model=List[HeroReadWithTeam])
async def read_heroes(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    heros = await crud.hero.read_multi(session=session, offset=offset, limit=limit)
    return heros


@router.get("/heroes/{hero_id}", response_model=HeroReadWithTeam)
async def read_hero(*, hero_id: int, session: Session = Depends(get_session)):
    hero = await crud.hero.read_by_id(session=session, id=hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.patch("/heroes/{hero_id}", response_model=HeroRead)
async def update_hero(*, session: Session = Depends(get_session), hero_id: int, hero: HeroUpdate):
    db_hero = await crud.hero.read_by_id(session=session, id=hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    updated_hero = await crud.hero.update(session=session, db_obj=db_hero, obj_in=hero)
    return updated_hero


@router.delete("/heroes/{hero_id}")
async def delete_hero(*, session: Session = Depends(get_session), hero_id: int):
    db_hero = await crud.hero.read_by_id(session=session, id=hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    await crud.hero.delete(session=session, id=hero_id)
    return {"ok": True}


@router.get("/heros/{hero_id}/abilities", response_model=List[HeroAbilityBase])
async def get_hero_abilities(*, session: Session = Depends(get_session), hero_id: int):
    statement = select(HeroAbilityLink).where(HeroAbilityLink.hero_id == hero_id)
    reslut = await session.exec(statement)
    return reslut.all()


@router.post("/hero-abilities", response_model=HeroAbilityBase)
async def create_hero_ability(*, session: Session = Depends(get_session), hero_ability_data: HeroAbilityCreateUpdate):
    db_hero_ability = await crud.hero_ability_link.create(session=session, obj_in=hero_ability_data)
    return db_hero_ability


@router.put("/hero-abilities", response_model=HeroAbilityBase)
async def update_hero_abilitie(*, session: Session = Depends(get_session), hero_ability_data: HeroAbilityCreateUpdate):
    db_hero_ability = await crud.hero_ability_link.read_by_id(
        session=session, id=(hero_ability_data.hero_id, hero_ability_data.ability_id)
    )
    if not db_hero_ability:
        raise HTTPException(status_code=404, detail="Ability is not associated to the given hero")

    updated_hero_ability = await crud.hero_ability_link.update(
        session=session, db_obj=db_hero_ability, obj_in=hero_ability_data
    )
    return updated_hero_ability


@router.delete("/heroes/{hero_id}/abilities/{ability_id}")
async def delete_hero_ability(*, session: Session = Depends(get_session), hero_id: int, ability_id: int):
    db_hero_ability = await crud.hero_ability_link.read_by_id(session=session, id=(hero_id, ability_id))
    if not db_hero_ability:
        raise HTTPException(status_code=404, detail="Ability is not associated to the given hero")
    await crud.hero_ability_link.delete(session=session, id=(hero_id, ability_id))
    return {"ok": True}
