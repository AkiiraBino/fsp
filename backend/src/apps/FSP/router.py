from fastapi import APIRouter
from fastapi.responses import JSONResponse
import sqlalchemy as sa
from typing import Annotated


from .schemas import CityResponseSchema

router = APIRouter(prefix="/cities", tags=["cities"])


@router.get("/")
async def get_city(
    starting_city: str,
    target_city: str
) -> CityResponseSchema:
    pass