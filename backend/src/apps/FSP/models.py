import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from src.apps.FSP.schemas import CitySchema, RoadSchema

from src.settings.db import Base


class City(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(unique=True)

    def to_read_model(self):
        return CitySchema(id=self.id, name=self.name)


class Road(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    previous_city: Mapped[int] = mapped_column(sa.ForeignKey("FSP_city.id"))
    next_city: Mapped[int] = mapped_column(sa.ForeignKey("FSP_city.id"))
    distance: Mapped[int]

    __table_args__ = (
        sa.UniqueConstraint("previous_city", "next_city", name="uix_road"),
    )

    def to_read_model(self):
        return RoadSchema(
            id=self.id,
            previous_city=self.previous_city,
            next_city=self.next_city,
            distance=self.distance,
        )
