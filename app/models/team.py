from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship, SQLModel

from app.models.common import TimestampModel

if TYPE_CHECKING:
    from app.models.hero import Hero, HeroRead


class TeamBase(TimestampModel):
    name: str = Field(index=True)
    headquarters: str


class Team(TeamBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: List["Hero"] = Relationship(back_populates="team", sa_relationship_kwargs={"lazy": "joined"})  # noqa: F821


class TeamCreate(SQLModel):
    name: str
    headquarters: str


class TeamRead(TeamBase):
    id: int


class TeamUpdate(SQLModel):
    name: str | None = None
    headquarters: str | None = None


class TeamReadWithHeroes(TeamRead):
    heroes: List["HeroRead"] = []
