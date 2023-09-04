from pydantic import BaseModel, Json


class CityResponseSchema(BaseModel):
    class DistanceResultSchema(BaseModel):
        target_city: str
        distance: int
        
    city: str
    result: DistanceResultSchema