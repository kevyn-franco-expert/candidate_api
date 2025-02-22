import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import candidates, calculator
from app.core.config import get_settings
from app.db.session import engine
from app.models import Base


def create_application() -> FastAPI:
    settings = get_settings()

    application = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    Base.metadata.create_all(bind=engine)

    application.include_router(
        candidates.router,
        prefix=f"{settings.API_V1_STR}/candidates",
        tags=["candidates"]
    )
    application.include_router(
        calculator.router,
        prefix=f"{settings.API_V1_STR}/calculator",
        tags=["calculator"]
    )
    return application


app = create_application()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
