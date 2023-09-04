from src.apps.utils import SQLAlchemyRepository
from src.apps.FSP.models import *


class CityRepository(SQLAlchemyRepository):
    model = City


class RoadRepository(SQLAlchemyRepository):
    model = Road
