from fastapi import FastAPI
from starlette.config import Config
from .config import Settings


config = Config(".env")  # parse .env file for env variables
DEFAULT_ENVIRONMENT = "local"
ENVIRONMENT = config("ENVIRONMENT", default=DEFAULT_ENVIRONMENT)
SHOW_DOCS_ENVIRONMENT = [DEFAULT_ENVIRONMENT]  # explicit list of allowed envs

app_configs = {"title": "FastApi Base"}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["openapi_url"] = None  # set url for docs as null

settings = Settings()
app = FastAPI(**app_configs)


@app.get("/")
async def main_route():
    return {"message": "Hey, It is me Goku"}


@app.get("/info")
async def info():
    return {"app_name": settings.app_name}
