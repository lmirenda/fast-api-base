from sqlalchemy.orm import sessionmaker
from sqlmodel import create_engine

from ..core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    try:
        session = SessionLocal()
        yield session
    finally:
        session.close()
