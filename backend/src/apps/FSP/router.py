from fastapi import APIRouter,  Depends
from fastapi.responses import JSONResponse
import sqlalchemy as sa
from typing import Annotated


from .schemas import FSPResponseSchema, CitySchema, RoadSchema
from .services import *
from .dependencies import *

router = APIRouter(prefix="/cities", tags=["cities"])



@router.get("/")
async def get_distance(
    started_city: str,
    target_city: str,
    find_distance_service: Annotated[FindDistanceService, Depends(find_distance_service)]
):
    result = await find_distance_service.get_smillest_distance(started_city, target_city)
    pass
    

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
