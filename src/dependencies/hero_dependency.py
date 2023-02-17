from fastapi import Depends
from sqlmodel import Session

from src.db.session import get_session
from src.repositories.hero_repository import HeroRepository


def get_hero_repository(session: Session = Depends(get_session)) -> HeroRepository:
    try:
        hero_repository = HeroRepository(session)
        yield hero_repository
    finally:
        session.close()
