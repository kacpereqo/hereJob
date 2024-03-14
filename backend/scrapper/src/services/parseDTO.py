from src.common.models.offert import OffertProvider
from src.services.justjJoinit.parseDTO import JustJoinItDTOParser


class ParserDTOFactory:

    @staticmethod
    def getParseDTO(data: dict[object], offertProvider: OffertProvider):
        match offertProvider:
            case OffertProvider.justjoinit:
                return JustJoinItDTOParser.parse(data)
            case _:
                raise ValueError("Invalid provider")
