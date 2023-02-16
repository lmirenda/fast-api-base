from typing import Optional

from sqlmodel import Field
from uuid import UUID, uuid4

from src.schemas.hero import HeroBase


class Hero(HeroBase, table=True):
    id: Optional[UUID] = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
