from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app import crud
from app.db import get_session
from app.models.ability import AbilityCreate, AbilityRead, AbilityUpdate

router = APIRouter()


@router.post("/abilities/", response_model=AbilityRead)
async def create_ability(*, session: Session = Depends(get_session), ability: AbilityCreate):
    db_ability = await crud.ability.create(session=session, obj_in=ability)
    return db_ability


@router.get("/abilities/", response_model=List[AbilityRead])
async def read_abilities(
    *,
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = 100,
):
    abilities = await crud.ability.read_multi(session=session, offset=offset, limit=limit)
    return abilities


@router.get("/abilities/{ability_id}", response_model=AbilityRead)
async def read_team(*, ability_id: int, session: Session = Depends(get_session)):
    ability = await crud.ability.read_by_id(session=session, id=ability_id)
    if not ability:
        raise HTTPException(status_code=404, detail="Ability not found")
    return ability


@router.patch("/abilities/{ability_id}", response_model=AbilityRead)
async def update_ability(*, session: Session = Depends(get_session), ability_id: int, ability: AbilityUpdate):
    db_ability = await crud.ability.read_by_id(session=session, id=ability_id)
    if not db_ability:
        raise HTTPException(status_code=404, detail="Ability not found")
    updated_ability = await crud.ability.update(session=session, db_obj=db_ability, obj_in=ability)
    return updated_ability


@router.delete("/abilities/{ability_id}")
async def delete_ability(*, session: Session = Depends(get_session), ability_id: int):
    db_ability = await crud.ability.read_by_id(session=session, id=ability_id)
    if not db_ability:
        raise HTTPException(status_code=404, detail="Ability not found")
    await crud.ability.delete(session=session, id=ability_id)
    return {"ok": True}
