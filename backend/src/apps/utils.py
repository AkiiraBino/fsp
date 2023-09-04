from abc import ABC, abstractmethod
from sqlalchemy import select


from src.settings.db import async_session_maker
from src.apps.models import *

class AbstractRepository(ABC):
    @abstractmethod
    async def get_all():
        raise NotImplementedError
    

class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def get_all(self):
        async with async_session_maker() as session:
            query = select(self.model)
            result = await session.execute(query)
            return result.scalars()