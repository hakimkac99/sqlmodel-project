"""init

Revision ID: 6c84d534d955
Revises: 
Create Date: 2023-12-09 23:33:12.555770

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel  # NEW

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "6c84d534d955"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "ability",
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "team",
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("headquarters", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_team_name"), "team", ["name"], unique=False)
    op.create_table(
        "hero",
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("(CURRENT_TIMESTAMP)"), nullable=False),
        sa.Column("first_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("last_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("team_id", sa.Integer(), nullable=True),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["team_id"],
            ["team.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_hero_first_name"), "hero", ["first_name"], unique=False)
    op.create_index(op.f("ix_hero_last_name"), "hero", ["last_name"], unique=False)
    op.create_table(
        "hero_ability_link",
        sa.Column("hero_id", sa.Integer(), nullable=False),
        sa.Column("ability_id", sa.Integer(), nullable=False),
        sa.Column("level", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["ability_id"],
            ["ability.id"],
        ),
        sa.ForeignKeyConstraint(
            ["hero_id"],
            ["hero.id"],
        ),
        sa.PrimaryKeyConstraint("hero_id", "ability_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("hero_ability_link")
    op.drop_index(op.f("ix_hero_last_name"), table_name="hero")
    op.drop_index(op.f("ix_hero_first_name"), table_name="hero")
    op.drop_table("hero")
    op.drop_index(op.f("ix_team_name"), table_name="team")
    op.drop_table("team")
    op.drop_table("ability")
    # ### end Alembic commands ###
