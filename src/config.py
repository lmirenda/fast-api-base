from pydantic import BaseSettings
from starlette.config import Config


class Settings(BaseSettings):
    APP_NAME = "FastApi Base"
    ALLOWED_CORS_ORIGINS: list[str]
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_PORT: str = ""
    DATABASE_HOSTNAME: str = ""
    POSTGRES_DB: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Define the base environment
DEFAULT_ENVIRONMENT = "local"
SHOW_DOCS_ENVIRONMENT = [DEFAULT_ENVIRONMENT]

config = Config(".env")
ENVIRONMENT = config("ENVIRONMENT", default=DEFAULT_ENVIRONMENT)
SHOW_DOCS_ENVIRONMENT = [DEFAULT_ENVIRONMENT]

# Create the fast api app config
settings = Settings()
APP_CONFIGS = {"title": settings.APP_NAME}
if ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    APP_CONFIGS["openapi_url"] = None
