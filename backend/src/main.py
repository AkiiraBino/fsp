import fastapi

from src.settings.const import BASE_URL
from src.apps.FSP.router import router as router_city

app = fastapi.FastAPI()
appv1 = fastapi.FastAPI()

appv1.include_router(router_city)


app.mount(BASE_URL, appv1)