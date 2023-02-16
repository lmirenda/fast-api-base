from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.exceptions import RequestValidationError

from src.dependencies.hero_repository_dependency import get_hero_repository
from src.models.hero import HeroRead, HeroCreate, HeroBase
from src.repositories.hero_repository import HeroRepository

router = APIRouter(
    prefix="/heroes",
    tags=["heroes"],
)


@router.get("/{name}/", response_model=HeroRead)
def get_hero_by_name(*, hero_repository: HeroRepository = Depends(get_hero_repository), name: str):
    hero = hero_repository.read_by_name(hero_name=name)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@router.post("/", response_model=HeroBase)
def create_hero(*, hero_repository: HeroRepository = Depends(get_hero_repository), hero: HeroCreate):
    try:
        hero_repository.create(hero=hero)
    except RequestValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    return hero


@router.get("/")
def get_all_heroes(
        *,
        hero_repository: HeroRepository = Depends(get_hero_repository),
        offset: int = 0,
        limit: int = Query(default=10, lte=20)
):
    return hero_repository.read_all(offset=offset, limit=limit)
