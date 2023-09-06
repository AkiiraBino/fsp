from fastapi import APIRouter, Depends
from typing import Annotated


from .schemas import FSPResponseSchema, CitySchema, RoadSchema, DifferenceSchema
from .services import *
from .dependencies import *

router = APIRouter(prefix="/cities", tags=["cities"])


@router.get("/")
async def get_distance(
    started_city: str,
    target_city: str,
    find_distance_service: Annotated[
        FindDistanceService, Depends(find_distance_service)
    ],
) -> FSPResponseSchema:
    result = await find_distance_service.get_smillest_distance(
        started_city, target_city
    )
    return {
        "city": started_city,
        "result": {"distance": result, "target_city": target_city},
    }


@router.get("/difference")
async def get_difference(
    city: str,
    find_distance_service: Annotated[
        FindDistanceService, Depends(find_distance_service)
    ],
) -> list[DifferenceSchema]:
    result = await find_distance_service.distance_difference(city)

    return result


@router.get("/city")
async def get_all_city(
    city_service: Annotated[CityService, Depends(city_service)]
) -> list[CitySchema]:
    result = await city_service.get_all_city()
    return result


@router.get("/road")
async def get_all_road(
    city_service: Annotated[RoadService, Depends(road_service)]
) -> list[RoadSchema]:
    result = await city_service.get_all_road()
    return result
