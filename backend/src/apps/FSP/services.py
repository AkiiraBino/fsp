from src.apps.utils import AbstractRepository

class CityService:
    def __init__(self, city_repo: AbstractRepository):
        self.city_repo = city_repo()

    async def get_all(self):
        result = await self.city_repo.get_all()
        return result