from typing import Optional

from sqlmodel import SQLModel
from uuid import UUID
from src.models.team import Team


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: UUID
    team: Optional[Team]


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
