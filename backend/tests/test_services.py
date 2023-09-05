import pytest

from src.apps.FSP.services import CityService, RoadService
from src.apps.FSP.repository import CityRepository, RoadRepository
from src.apps.FSP.schemas import CitySchema, RoadSchema


@pytest.mark.asyncio
async def test_city_service():
    city_service = CityService(CityRepository)
    result = await city_service.get_all_city()
    assert result == [
        CitySchema(id=1, name='Renton'),
        CitySchema(id=2, name='SoDo'),
        CitySchema(id=3, name='Factoria'), 
        CitySchema(id=4, name='Issaquah'),
        CitySchema(id=5, name='Seattle'), 
        CitySchema(id=6, name='Bellevue'), 
        CitySchema(id=7, name='Redmond'), 
        CitySchema(id=8, name='Eastlake'), 
        CitySchema(id=9, name='Northup')]


@pytest.mark.asyncio
async def test_road_service():
    road_service = RoadService(RoadRepository)
    result = await road_service.get_all_road()
    assert result == [
        RoadSchema(id=1, previous_city=1, next_city=2, distance=12), 
        RoadSchema(id=2, previous_city=1, next_city=3, distance=8), 
        RoadSchema(id=3, previous_city=1, next_city=4, distance=12), 
        RoadSchema(id=4, previous_city=2, next_city=3, distance=8), 
        RoadSchema(id=5, previous_city=2, next_city=5, distance=1), 
        RoadSchema(id=6, previous_city=3, next_city=6, distance=2), 
        RoadSchema(id=7, previous_city=3, next_city=7, distance=9), 
        RoadSchema(id=8, previous_city=3, next_city=4, distance=10), 
        RoadSchema(id=9, previous_city=4, next_city=7, distance=14), 
        RoadSchema(id=10, previous_city=5, next_city=8, distance=2), 
        RoadSchema(id=11, previous_city=8, next_city=9, distance=8), 
        RoadSchema(id=12, previous_city=6, next_city=9, distance=1), 
        RoadSchema(id=13, previous_city=6, next_city=7, distance=8), 
        RoadSchema(id=14, previous_city=9, next_city=7, distance=5)]
    
    