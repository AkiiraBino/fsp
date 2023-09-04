from pydantic import BaseModel, Json


class CitySchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class RoadSchema(BaseModel):
    id: int
    previous_city: int
    next_city: int
    distance: int


class FSPResponseSchema(BaseModel):
    class DistanceResultSchema(BaseModel):
        target_city: str
        distance: int
        
    city: str
    result: DistanceResultSchema