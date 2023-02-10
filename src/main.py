from fastapi import FastAPI
from .core.config import APP_CONFIGS, settings


app = FastAPI(**APP_CONFIGS)


@app.get("/")
async def main_route():
    return {"message": "Hey, It is me Goku"}


@app.get("/info")
async def info():
    return {"app_name": settings.app_name}
