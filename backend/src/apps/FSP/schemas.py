from pydantic import BaseModel, ConfigDict, Field


class CitySchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class RoadSchema(BaseModel):
    id: int
    previous_city: int
    next_city: int
    distance: int

    model_config = ConfigDict(from_attributes=True)


class FSPResponseSchema(BaseModel):
    class DistanceResultSchema(BaseModel):
        target_city: str
        distance: int

    city: str
    result: DistanceResultSchema
