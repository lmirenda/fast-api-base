from fastapi import APIRouter, Depends, HTTPException
from fastapi.exceptions import RequestValidationError

from src.db.session import SessionLocal, get_session
from src.models import Hero
from src.models.hero import HeroRead, HeroCreate

router = APIRouter(
    prefix="/heroes",
    tags=["heroes"],
)


@router.get("/{name}/")
def get_hero_by_name(*, session: SessionLocal = Depends(get_session), name: str):
    db_hero = session.query(Hero).filter(Hero.name == name).first()
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero = Hero.from_orm(db_hero)
    return hero


@router.post("/", response_model=HeroRead)
def create_hero(*, session: SessionLocal = Depends(get_session), hero: HeroCreate):
    try:
        db_hero = Hero.from_orm(hero)
    except RequestValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@router.get("/")
def get_all_heroes(*, session: SessionLocal = Depends(get_session)):
    db_heroes = session.query(Hero).all()
    heroes = [Hero.from_orm(hero) for hero in db_heroes]
    return heroes
