from datetime import datetime

from pydantic import BaseModel


class Offert(BaseModel):
    id: int
    title: str
    description: str
    price: float
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime
