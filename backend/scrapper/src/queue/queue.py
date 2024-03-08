import redis
import rq
from src.services.distance import distanceService
from toolz import pipe


def queue_task( data: dict[str, str]) -> None:
    pipe(
        distanceService.pipe,
    )

class TaskQueue():

    instances: object = None


    def __init__(self) -> None:
        if TaskQueue.instances is not None:
            raise Exception("This class is a singleton!")
        else:
            TaskQueue.instances = self
            self.redis_conn = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
            self.queue = rq.Queue(connection=self.redis_conn)



    def add_task(self, task: dict[str, str] | list[dict[str,str]]) -> None:
        """
        Add task to queue

        Keyword arguments:
        task:dict[str,str] - task to be added to queue

        return: None
        """

        if isinstance(task, list) or isinstance(task, tuple):
            self.queue.enqueue_many(
                [
                    self.queue.prepare_data(queue_task, ((t),),result_ttl=0) for t in task
                ]
            )
        else:
            self.queue.enqueue(queue_task, task,result_ttl=0)