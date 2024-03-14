import os

import redis
import rq
from src.common.models.offert import OffertProvider
from src.queue.queueTask import queue_task


class TaskQueue:

    instances: object = None

    def __init__(self) -> None:
        if TaskQueue.instances is not None:
            raise Exception("This class is a singleton!")
        else:
            TaskQueue.instances = self

            host, port = self.load_env()

            self.redis_conn = redis.StrictRedis(host=host, port=port, db=0)
            self.queue = rq.Queue("Scrapper_queue", connection=self.redis_conn)

    def load_env(self) -> tuple[str, str]:
        """
        Load environment variables

        return: tuple[str,str] - tuple with environment variables
        """
        port = os.environ.get("REDIS_PORT")
        host = os.environ.get("REDIS_HOST")

        return host, port

    def add_task(
        self,
        task: dict[str, str] | list[dict[str, str]],
        offertProvider: OffertProvider,
    ) -> None:
        """
        Add task to queue

        Keyword arguments:
        task:dict[str,str] - task to be added to queue

        return: None
        """

        if isinstance(task, list) or isinstance(task, tuple):
            map(
                lambda t: t.update({"offert_provider": offertProvider.value}), task
            )  # set offert_provider for each task

            self.queue.enqueue_many(
                [
                    self.queue.prepare_data(queue_task(), ((t),), result_ttl=0)
                    for t in task
                ]
            )

        else:
            task["offert_provider"] = (
                offertProvider.value
            )  # set offert_provider for task
            self.queue.enqueue(queue_task, task, result_ttl=0)
