from typing import Optional

from sqlmodel import Field, SQLModel
import uuid as uuid_pkg


class Hero(SQLModel, table=True):
    id: Optional[uuid_pkg.UUID] = Field(
        default_factory=uuid_pkg.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )
    name: str
    secret_name: str
    age: Optional[int] = None
