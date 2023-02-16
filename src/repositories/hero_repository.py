from typing import Optional

from fastapi import Query
from pydantic.types import UUID
from sqlmodel import Session, select

from src.models import Hero
from src.models.hero import HeroCreate, HeroRead, HeroUpdate
from src.repositories.base_repository import BaseRepository


class HeroRepository(BaseRepository):

    def __init__(self, db: Session):
        self.db = db

    def create(self, hero: HeroCreate) -> Hero:
        hero_db = Hero.from_orm(hero)
        self.db.add(hero_db)
        self.db.commit()
        self.db.refresh(hero_db)
        return hero_db

    def read(self, hero_uuid: UUID) -> Optional[HeroRead]:
        return self.db.get(Hero, hero_uuid)

    def read_by_name(self, hero_name: str) -> Optional[Hero]:
        return self.db.query(Hero).filter(Hero.name == hero_name).first()

    def update(self, hero: HeroUpdate, hero_id: UUID) -> None:
        db_hero = self.read(hero_id)
        hero_data = hero.dict(exclude_unset=True)
        for key, value in hero_data.items():
            setattr(db_hero, key, value)
        self.db.add(db_hero)
        self.db.commit()
        self.db.refresh(db_hero)
        return db_hero

    def delete(self, hero_id: UUID) -> None:
        self.db.delete(self.read(hero_id))
        self.db.commit()

    def read_all(self, offset: int = 0, limit: int = Query(default=1, lte=20)) -> list[Hero]:
        return self.db.exec(select(Hero).offset(offset).limit(limit)).all()
