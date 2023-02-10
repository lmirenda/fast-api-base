from pydantic import BaseSettings


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
