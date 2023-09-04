from src.apps.FSP.services import CityService
from src.apps.FSP.repository import CityRepository

def city_service():
    return CityService(CityRepository)