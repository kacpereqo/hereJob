import redis
from rq import Queue

r = redis.Redis(host="localhost", port=6379, decode_responses=True)

q = Queue(connection=r)
