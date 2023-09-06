from src.apps.utils import SQLAlchemyRepository, SQLAlcemyRepositoryWithTwoModels
from src.apps.FSP.models import *


class CityRepository(SQLAlchemyRepository):
    model = City


class RoadRepository(SQLAlchemyRepository):
    model = Road


class CityWithRoadRepository(SQLAlcemyRepositoryWithTwoModels):
    model_1 = City
    model_2 = Road
