from fastapi import APIRouter
from src.common.models.offert import Offert

router = APIRouter(prefix="/offerts")


@router.get("/")
async def read_root() -> list[Offert]:
    return {"Hello": "World"}


@router.get("/{offert_id}")
async def read_offert(offert_id: int) -> Offert:
    return {"offert_id": offert_id}


@router.get("/pagination")
async def read_pagination(start: int = 0, limit: int = 10) -> list[Offert]:
    return {"pagination": "pagination"}
