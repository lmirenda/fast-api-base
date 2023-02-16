from typing import Optional

from sqlmodel import Field, SQLModel
import uuid as uuid_pkg


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Optional[int] = None


class Hero(HeroBase, table=True):
    id: Optional[uuid_pkg.UUID] = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: uuid_pkg.UUID


class HeroUpdate(SQLModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None

