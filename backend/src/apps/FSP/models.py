import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.settings.db import Base


class City(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column()


class Road(Base):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    previous_city: Mapped[int] = mapped_column(sa.ForeignKey("FSP_city.id"))
    next_city: Mapped[int] = mapped_column(sa.ForeignKey("FSP_city.id"))
    distance: Mapped[int]

    __table_args__ = (
        sa.UniqueConstraint("previous_city", "next_city", name="uix_road"),
    )