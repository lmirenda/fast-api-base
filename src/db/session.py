from sqlmodel import create_engine, Session
from sqlalchemy.orm import sessionmaker
from ..core.config import get_settings

settings = get_settings()

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    try:
        with Session(engine) as session:
            yield session
    finally:
        session.close()
