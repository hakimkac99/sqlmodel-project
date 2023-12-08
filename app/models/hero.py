from typing import TYPE_CHECKING, List, Optional

from sqlmodel import Field, Relationship, SQLModel

from app.models.ability import Ability
from app.models.link_models import HeroAbilityLink

if TYPE_CHECKING:
    from app.models.team import Team, TeamRead


class HeroBase(SQLModel):
    first_name: str = Field(index=True)
    last_name: str = Field(index=True)
    age: int | None
    team_id: int | None = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team: Optional["Team"] = Relationship(back_populates="heroes")
    abilities: List["Ability"] = Relationship(back_populates="heroes", link_model=HeroAbilityLink)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    first_name: str | None = None
    last_name: str | None = None
    age: int | None = None
    team_id: int | None = None


class HeroReadWithTeam(HeroRead):
    team: Optional["TeamRead"] = None
