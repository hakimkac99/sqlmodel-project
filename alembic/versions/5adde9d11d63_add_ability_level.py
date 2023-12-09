"""add ability level

Revision ID: 5adde9d11d63
Revises: 9da90d5443a2
Create Date: 2023-12-09 00:34:43.833785

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel  # NEW

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5adde9d11d63"
down_revision: Union[str, None] = "9da90d5443a2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("hero_ability_link", sa.Column("level", sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("hero_ability_link", "level")
    # ### end Alembic commands ###
