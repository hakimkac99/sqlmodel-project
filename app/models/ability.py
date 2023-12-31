from typing import TYPE_CHECKING, List

from sqlmodel import Field, Relationship, SQLModel

from app.models.common import TimestampModel

if TYPE_CHECKING:
    from app.models.hero import Hero

from app.models.link_models import HeroAbilityLink


class AbilityBase(TimestampModel):
    name: str
    description: str


class Ability(AbilityBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    heroes: List["Hero"] = Relationship(back_populates="abilities", link_model=HeroAbilityLink)


class AbilityCreate(SQLModel):
    name: str
    description: str


class AbilityRead(AbilityBase):
    id: int


class AbilityUpdate(SQLModel):
    name: str | None
    description: str | None
