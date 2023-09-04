from fastapi import APIRouter,  Depends
from fastapi.responses import JSONResponse
import sqlalchemy as sa
from typing import Annotated


from .schemas import FSPResponseSchema, CitySchema
from .services import CityService
from .dependencies import city_service

router = APIRouter(prefix="/cities", tags=["cities"])



@router.get("/")
async def get_distance(
    started_city: str,
    target_city: str,
    city_service: Annotated[CityService, Depends(city_service)]
) -> FSPResponseSchema:
    pass
    





@router.get("/all")
async def get_all_city(
    city_service: Annotated[CityService, Depends(city_service)]
) -> list[CitySchema]:
    result = await city_service.get_all()
    return result
