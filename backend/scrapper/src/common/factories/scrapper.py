from abc import ABC, abstractmethod

from src.queue.queue import TaskQueue


class Scrapper(ABC):
    def __init__(self) -> None:
        self.queue = TaskQueue()

    @abstractmethod
    def scrap(self) -> None:
        """
        Scrap data from website then sends it to queue to be processed
        """
        pass

    def add_to_queue(self, data: dict[str, str] | list[dict[str,str]]) -> None:
        """ "
        Add data to redis queue to be processed by workers

        Keyword arguments:
        data:dict[str,str] | list[dict[str,str]] - data to be added to queue

        return: None
        """
        self.queue.add_task(data)
        print("add_to_queue") 
