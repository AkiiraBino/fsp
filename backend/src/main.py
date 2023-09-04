import fastapi

from src.settings.const import BASE_URL

app = fastapi.FastAPI()
appv1 = fastapi.FastAPI()


app.mount(BASE_URL, appv1)