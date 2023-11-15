from sqlmodel import SQLModel, Field


class HeroBase(SQLModel):
    name: str = Field(index=True)
    secret_name: str
    age: int | None


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: str | None = None
    secret_name: str | None = None
    age: int | None = None