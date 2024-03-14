from typing import NamedTuple

from src.common.dto.justJoinIt import justJoinItDTO
from src.common.models.offert import Offert, OffertProvider


class PipeData(NamedTuple):
    end_offert: Offert
    offert_provider: OffertProvider
    data: justJoinItDTO
