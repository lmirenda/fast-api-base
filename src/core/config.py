from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME = "FastApi Base"
    ALLOWED_CORS_ORIGINS: list[str]
    POSTGRES_USER: str = ""
    POSTGRES_PASSWORD: str = ""
    POSTGRES_PORT: str = ""
    DATABASE_HOSTNAME: str = ""
    POSTGRES_DB: str = ""
    ENVIRONMENT = "local"
    SHOW_DOCS_ENVIRONMENT = ["local"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create the fast api app config
settings = Settings()
APP_CONFIGS = {"title": settings.APP_NAME}
if settings.ENVIRONMENT not in settings.SHOW_DOCS_ENVIRONMENT:
    APP_CONFIGS["openapi_url"] = None
