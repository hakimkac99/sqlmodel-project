from sqlmodel import Field, Relationship, SQLModel

from app.models.team import Team


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None
    team_id: int | None = Field(default=None, foreign_key="team.id")


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    team: Team | None = Relationship(back_populates="heroes")


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None
    team_id: int | None = None
