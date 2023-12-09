from datetime import datetime

from sqlalchemy import func, text
from sqlmodel import Field, SQLModel


class TimestampModel(SQLModel):
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP")},
    )

    updated_at: datetime = Field(
        default_factory=datetime.utcnow,
        nullable=False,
        sa_column_kwargs={"server_default": text("CURRENT_TIMESTAMP"), "onupdate": func.now()},
    )
