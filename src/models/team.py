from typing import Optional

from sqlmodel import Field, SQLModel, Relationship
from uuid import UUID, uuid4


class Team(SQLModel, table=True):
    id: Optional[UUID] = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="team")
