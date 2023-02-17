from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .core.config import APP_CONFIGS, settings
from .internal import status
from .routers import heroes, items

app = FastAPI(**APP_CONFIGS)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(items.router, prefix=settings.API_V1_STR)
app.include_router(heroes.router, prefix=settings.API_V1_STR)
if settings.ENVIRONMENT in settings.SHOW_DOCS_ENVIRONMENT:
    app.include_router(status.router, prefix=settings.API_V1_STR)
