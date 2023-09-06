from src.apps.FSP.services import *
from src.apps.FSP.repository import *


def city_service():
    return CityService(CityRepository)


def road_service():
    return RoadService(RoadRepository)


def find_distance_service():
    return FindDistanceService(CityRepository, RoadRepository, CityWithRoadRepository)
