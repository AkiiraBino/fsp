from dotenv import load_dotenv
import os
from .const import BASE_DIR

dotenv_path = BASE_DIR + "/.env"
load_dotenv(dotenv_path)

DB_HOST = os.environ.get("DB_HOST")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


SQLALCHEMY_ASYNC_DATABASE_URL = (
    f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"
)
