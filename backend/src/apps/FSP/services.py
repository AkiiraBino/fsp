import asyncio
import math
from fastapi import HTTPException
from sqlalchemy import text

from src.apps.utils import AbstractRepository
from src.apps.FSP.schemas import CitySchema, RoadSchema
from src.settings.db import async_session_maker

class CityService:
    def __init__(self, city_repo: AbstractRepository):
        self.city_repo: AbstractRepository = city_repo()

    async def get_all_city(self) -> list:
        result = await self.city_repo.get_all()
        result = [row[0].to_read_model() for row in result]
        return result
    
    async def get_city_with_filtered(self, filters: dict) -> list:
        result = await self.city_repo.get_with_filtered(filters)
        result = [row[0].to_read_model() for row in result]
        return result


class RoadService:
    def __init__(self, road_repo: AbstractRepository):
        self.road_repo = road_repo()

    async def get_all_road(self) -> list:
        result = await self.road_repo.get_all()
        result = [row[0].to_read_model() for row in result]
        return result


class FindDistanceService(CityService, RoadService):
    def __init__(self, city_repo: AbstractRepository, road_repo: AbstractRepository):
        self.city_repo: AbstractRepository = city_repo()
        self.road_repo: AbstractRepository = road_repo()
        self.cities: list[CitySchema] = asyncio.run(self.get_all_city())
        self.roads: list[RoadSchema] = asyncio.run(self.get_all_road())

    def find_min(self, lenght_roads: dict, visited_cities: set) -> int:
        result = -1
        minimum = math.inf
        for city, lenght in lenght_roads.items():
            if lenght < minimum and city not in visited_cities:
                minimum = lenght
                result = city

        return result

    def get_link_road(self, current: int) -> dict:
        for road in self.roads:
            if road.previous_city == current:
                yield {"id": road.next_city, "distance": road.distance}
            elif road.next_city == current:
                yield {"id": road.previous_city, "distance": road.distance}

    def validation_city(self, start_city, end_city="Renton"):
        name_cities = set()
        [name_cities.add(city.name) for city in self.cities]

        if start_city not in name_cities or end_city not in name_cities:
            raise HTTPException(404, "start city or end city not found")

    async def get_smillest_distance(self, start_city: str, end_city: str) -> int:
        self.validation_city(start_city, end_city)
        current = 0
        lenght_roads = {}
        end_id = 0

        for city in self.cities:
            if city.name != start_city:
                lenght_roads[city.id] = math.inf
            else:
                lenght_roads[city.id] = 0
                current = city.id

            if city.name == end_city:
                end_id = city.id

        visited_cities = {current}

        while current != -1:
            for road in self.get_link_road(current):
                if road["id"] not in visited_cities:
                    lenght = lenght_roads[current] + road["distance"]

                    if lenght_roads[road["id"]] > lenght:
                        lenght_roads[road["id"]] = lenght

            current = self.find_min(lenght_roads, visited_cities)

            if end_id in visited_cities:
                return lenght_roads[end_id]

            if current != -1:
                visited_cities.add(current)


    async def distance_difference(self, city):
        self.validation_city(city)
        async with async_session_maker() as session:
            query = text(f"""
                            WITH neighboring_cities as (SELECT 
                            "FSP_city".name as city, 
                            (
                                SELECT "FSP_city".name 
                                FROM "FSP_city"
                                WHERE "FSP_road".next_city = "FSP_city".id
                            ) as target_city,
                            "FSP_road".distance as distance
                            FROM "FSP_city" 
                            JOIN "FSP_road" on "FSP_road".previous_city = "FSP_city".id
                            WHERE "FSP_city".name = \'{city}\')
                            SELECT *,
                            ABS(LEAD(distance) OVER(PARTITION BY city ORDER BY target_city) - distance) 
                            FROM neighboring_cities;
                        """)
            result = await session.execute(query)
            result = [
                    {
                        "city": res[0],
                        "target_city": res[1],
                        "distance": res[2],
                        "difference_with_next": res[3]
                    } 
                    for res in result.all()
                ]
            return result