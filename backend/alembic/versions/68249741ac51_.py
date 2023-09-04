"""empty message

Revision ID: 68249741ac51
Revises: 3449c4fc92fa
Create Date: 2023-09-03 23:02:19.712849

"""
from alembic import op
import sqlalchemy as sa

#migration city into table FSP_city

data = [
"'Renton'",
"'SoDo'",
"'Factoria'",
"'Issaquah'",
"'Seattle'",
"'Bellevue'",
"'Redmond'",
"'Eastlake'",
"'Northup'",
]


# revision identifiers, used by Alembic.
revision = '68249741ac51'
down_revision = '3449c4fc92fa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    for i in data:
        op.execute(f'INSERT INTO "FSP_city" (name) VALUES ({i});')
    pass


def downgrade() -> None:
    for i in data:
        op.execute(f'DELETE from "FSP_city" where name={i}')
    pass
