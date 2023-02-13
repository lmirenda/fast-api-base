from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.core.config import settings


POSTGRES_USER: str = settings.POSTGRES_USER
POSTGRES_PASSWORD: str = settings.POSTGRES_PASSWORD
POSTGRES_PORT: str = settings.POSTGRES_PORT
DATABASE_HOSTNAME: str = settings.DATABASE_HOSTNAME
POSTGRES_DB: str = settings.POSTGRES_DB
ENVIRONMENT = settings.ENVIRONMENT
SHOW_DOCS_ENVIRONMENT = settings.SHOW_DOCS_ENVIRONMENT

SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DATABASE_HOSTNAME}:{POSTGRES_PORT}/{POSTGRES_DB} "

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

