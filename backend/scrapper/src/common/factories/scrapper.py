from abc import ABC, abstractmethod


class Scrapper(ABC):

    @abstractmethod
    def scrap(self) -> None:
        """
        Scrap data from website then sends it to queue to be processed
        """
        return {}

    def add_to_queue(self, data: dict[str, str]) -> None:
        """ "
        Add data to redis queue to be processed by workers

        Keyword arguments:
        data:dict[str,str] - data to be added to queue

        return: None
        """

        print("add_to_queue")
