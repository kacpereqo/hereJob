from src.common.models.offert import OffertProvider
from src.common.schemas.pipeData import PipeData
from src.services.parseDTO import ParserDTOFactory
from toolz import pipe

from backend.scrapper.src.services.geo import distanceService


def queue_task(offertProvider: OffertProvider) -> None:
    def innner(data: dict[object]):

        dto = ParserDTOFactory.getParseDTO(data, offertProvider)

        pipeData = PipeData(
            dto=dto,
            offertProvider=offertProvider,
        )
        return pipe(pipeData, (), distanceService.pipe, sexsex)
