import asyncio
from src.apps.utils import AbstractRepository

class CityService:
    def __init__(self, city_repo: AbstractRepository):
        self.city_repo = city_repo()

    async def get_all_city(self):
        result = await self.city_repo.get_all()
        result = [row[0].to_read_model() for row in result]
        return result
    

class RoadService:
    def __init__(self, road_repo: AbstractRepository):
        self.road_repo = road_repo()
    
    async def get_all_road(self):
        result = await self.road_repo.get_all()
        result = [row[0].to_read_model() for row in result]
        return result
    

class FindDistanceService(CityService, RoadService):
    def __init__(self, city_repo: AbstractRepository, road_repo: AbstractRepository):
        self.city_repo = city_repo()
        self.road_repo = road_repo()
        self.city = asyncio.run(self.get_all_city())
        self.road = asyncio.run(self.get_all_road())

    async def get_smillest_distance(self, start_city, end_city):
        pass