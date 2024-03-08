import requests
from orjson import loads
from src.common.factories.scrapper import Scrapper


class JustJoinItScrapper(Scrapper):
    def __init__(self) -> None:
        super().__init__()
        print("init JustJoinItScrapper")

        self._base_url = "https://api.justjoin.it/v2/user-panel/offers"

        self._params: dict[str, str | int] = {
            "page": 1,
            "sortBy": "published",
            "orderBy": "DESC",
            "perPage": 100,
            "salaryCurrencies": "EUR",
        }

        self._headers: dict[str, str] = {
            "x-snow": "eyJ1c2VySWQiOiJkNDRkMjZiZi1hOTQzLTRlNjUtYTI4Mi05MTAzYzQ2ZWRkNDAiLCJzZXNzaW9uSWQiOiIxZTRkNzZmYS03ZGRlLTQzNzYtYjJlMy1iZGNlZThlYTkzYjIifQ==",
            "Version": "2",
        }

    def scrap(self) -> None:
        print("JustJoinItScrapper scrap")

        r = requests.get(self._base_url, params=self._params, headers=self._headers)
        json = loads(r.text)
        # total_pages = json["meta"]["totalPages"]
        total_pages = 1

        for page in range(1, total_pages + 1):
            self._params["page"] = page

            r = requests.get(self._base_url, params=self._params, headers=self._headers)
            offerts = loads(r.text)["data"]

            self.add_to_queue(offerts)
