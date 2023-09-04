from pydantic import BaseModel, Field, Json


class CitySchema(BaseModel):
    id: int
    name: str = Field(max_length=200)

    class Config:
        from_attributes = True


class RoadSchema(BaseModel):
    id: int
    previous_city: int
    next_city: int
    distance: int

    class Config:
        from_attributes = True


class FSPResponseSchema(BaseModel):
    class DistanceResultSchema(BaseModel):
        target_city: str
        distance: int

    city: str
    result: DistanceResultSchema
