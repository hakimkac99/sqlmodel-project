from sqlmodel import Field, SQLModel

from app.models.common import TimestampModel


class HeroAbilityBase(TimestampModel):
    hero_id: int = Field(foreign_key="hero.id", primary_key=True)
    ability_id: int = Field(foreign_key="ability.id", primary_key=True)
    level: int = Field(default=1, ge=1, le=9)


class HeroAbilityLink(HeroAbilityBase, table=True):
    __tablename__ = "hero_ability_link"


class HeroAbilityCreateUpdate(SQLModel):
    hero_id: int
    ability_id: int
    level: int = Field(default=1, ge=1, le=9)
