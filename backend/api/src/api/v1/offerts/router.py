from fastapi import APIRouter
from src.common.models.offert import Offert

router = APIRouter(prefix="/offerts")


@router.get("/{offert_id}", response_model=Offert, description="Get offert by id")
async def read_offert(offert_id: int):
    return {"offert_id": offert_id}


@router.get(
    "/pagination",
    response_model=list[Offert],
    description="""Get offerts from ceratin range [start, limit] limit cannot be greater than 100 compared to start""",
)
async def read_pagination(start: int = 0, limit: int = 10):
    return {"pagination": "pagination"}
