"""empty message

Revision ID: 3449c4fc92fa
Revises: 
Create Date: 2023-09-03 23:02:00.856212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "3449c4fc92fa"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "FSP_city",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "FSP_road",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("previous_city", sa.Integer(), nullable=False),
        sa.Column("next_city", sa.Integer(), nullable=False),
        sa.Column("distance", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["next_city"],
            ["FSP_city.id"],
        ),
        sa.ForeignKeyConstraint(
            ["previous_city"],
            ["FSP_city.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("previous_city", "next_city", name="uix_road"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("FSP_road")
    op.drop_table("FSP_city")
    # ### end Alembic commands ###
