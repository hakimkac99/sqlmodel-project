from sqlmodel import Field, SQLModel


class HeroAbilityLink(
    SQLModel,
    table=True,
):
    __tablename__ = "hero_ability_link"
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
    ability_id: int | None = Field(default=None, foreign_key="ability.id", primary_key=True)
