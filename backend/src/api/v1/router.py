import jobOffert.router
from fastapi import APIRouter


def include_routers(a: str) -> APIRouter:
    router = APIRouter()
    router.include_router(
        jobOffert.router.router, tags=["jobOffert"], prefix="/jobOffert"
    )
    return router
