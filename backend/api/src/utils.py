from fastapi import FastAPI
from src.api.v1.offerts import router as v1_offerts_router

BASE_URL = "/api"
# jestem chory 11.03.2024


def include_routers(app: FastAPI) -> None:
    app.include_router(
        v1_offerts_router.router, tags=["offerts"], prefix=f"{BASE_URL}/v1"
    )


def create_app() -> FastAPI:
    app = FastAPI(prefix="/api")
    include_routers(app)
    return app
