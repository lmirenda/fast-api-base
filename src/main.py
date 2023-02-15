from fastapi import FastAPI, Query, Depends
from .core.config import APP_CONFIGS, settings
from .routers import items
from .internal import status

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
if settings.ENVIRONMENT in settings.SHOW_DOCS_ENVIRONMENT:
    app.include_router(status.router, prefix=settings.API_V1_STR)
