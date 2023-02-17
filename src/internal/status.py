from fastapi import APIRouter

from ..core.config import settings

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)


@router.get("/info")
async def info():
    return {"app_name": settings.APP_NAME}


@router.get("/database")
async def database():
    return {"database": "OK"}
