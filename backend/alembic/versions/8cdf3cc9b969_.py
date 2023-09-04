"""empty message

Revision ID: 8cdf3cc9b969
Revises: 68249741ac51
Create Date: 2023-09-03 23:29:09.162626

"""
from alembic import op
import sqlalchemy as sa

data = [
    {"city_1": "'Renton'", "city_2": "'SoDo'", "distance": 12},
    {"city_1": "'Renton'", "city_2": "'Factoria'", "distance": 8},
    {"city_1": "'Renton'", "city_2": "'Issaquah'", "distance": 12},
    {"city_1": "'SoDo'", "city_2": "'Factoria'", "distance": 8},
    {"city_1": "'SoDo'", "city_2": "'Seattle'", "distance": 1},
    {"city_1": "'Factoria'", "city_2": "'Bellevue'", "distance": 2},
    {"city_1": "'Factoria'", "city_2": "'Redmond'", "distance": 9},
    {"city_1": "'Factoria'", "city_2": "'Issaquah'", "distance": 10},
    {"city_1": "'Issaquah'", "city_2": "'Redmond'", "distance": 14},
    {"city_1": "'Seattle'", "city_2": "'Eastlake'", "distance": 2},
    {"city_1": "'Eastlake'", "city_2": "'Northup'", "distance": 8},
    {"city_1": "'Bellevue'", "city_2": "'Northup'", "distance": 1},
    {"city_1": "'Bellevue'", "city_2": "'Redmond'", "distance": 8},
    {"city_1": "'Northup'", "city_2": "'Redmond'", "distance": 5},
]

# revision identifiers, used by Alembic.
revision = "8cdf3cc9b969"
down_revision = "68249741ac51"
branch_labels = None
depends_on = None


def upgrade() -> None:
    for i in data:
        conn = op.get_bind()
        previous_city = conn.execute(
            sa.text(f"SELECT id FROM \"FSP_city\" WHERE name={i['city_1']}")
        )
        previous_city = previous_city.fetchall()[0][0]
        next_city = conn.execute(
            sa.text(f"SELECT id FROM \"FSP_city\" WHERE name={i['city_2']}")
        )
        next_city = next_city.fetchall()[0][0]
        op.execute(
            f"""
                INSERT INTO "FSP_road" 
                (previous_city, next_city, distance) 
                VALUES (
                    {previous_city},
                    {next_city},
                    {i["distance"]}
                    );
            """
        )
    pass


def downgrade() -> None:
    pass
