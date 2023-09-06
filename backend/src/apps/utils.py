from abc import ABC, abstractmethod
from sqlalchemy import select
from sqlalchemy.orm import aliased


from src.settings.db import async_session_maker
from src.apps.models import *


class AbstractRepository(ABC):
    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def get_deffirence(self, city):
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_all(self):
        async with async_session_maker() as session:
            query = select(self.model)
            result = await session.execute(query)
            return result.all()

    async def get_deffirence(self, city):
        raise NotImplementedError


class SQLAlcemyRepositoryWithTwoModels(AbstractRepository):
    model_1 = None
    model_2 = None

    async def get_all():
        raise NotImplementedError

    async def get_deffirence(self, city):
        async with async_session_maker() as session:
                cities = aliased(self.model_1)
                cities_2 = aliased(self.model_1)
                Roads = aliased(self.model_2)

                neighboring_cities = (select(
                    cities.name.label("city"),
                    cities_2.name.label("target_city"),
                    Roads.distance.label("distance")
                )
                .join(Roads, Roads.previous_city == cities.id)
                .join(cities_2, cities_2.id == Roads.next_city)
                .filter(cities.name == city)).cte("neighboring_cities")

                query = (
                    select(
                            neighboring_cities,
                            sa.func.lead(neighboring_cities.c.distance)
                            .over(
                                    partition_by=neighboring_cities.c.city,
                                    order_by=neighboring_cities.c.target_city
                                )
                            - neighboring_cities.c.distance
                        )
                        
                    )
                
                result = await session.execute(query)
                return result.all()
