from typing import Any

from src.common.dto.justJoinIt import justJoinItDTO


class JustJoinItDTOParser:
    @staticmethod
    def parse(data: dict[str, Any]) -> justJoinItDTO:

        data["employmentTypes"] = [
            {
                "salaryTo": salary.get("to", 0),
                "salaryFrom": salary.get("from", 0),
                "currency": salary.get("currency", "pln"),
                "type": salary.get("type", "permanent"),
            }
            for salary in data.get("employmentTypes", [])
        ]

        return justJoinItDTO(**data)
