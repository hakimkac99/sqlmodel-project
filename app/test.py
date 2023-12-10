import time
from datetime import datetime

from sqlmodel import Field, SQLModel


class User(SQLModel):
    name: str = Field(default=None)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


user = User(name="Hakim")
print(user.model_dump())
time.sleep(5)
user.name = "Hakim New"
print(user.model_dump())
