from typing import Optional

from sqlmodel import Field, Relationship
from uuid import UUID, uuid4

from src.models.team import Team
from src.schemas.hero import HeroBase


class Hero(HeroBase, table=True):
    id: Optional[UUID] = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    team_id: Optional[UUID] = Field(default=None, foreign_key="team.id")
    team: Optional[Team] = Relationship(back_populates="heroes")
