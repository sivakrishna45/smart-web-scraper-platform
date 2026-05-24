import redis
import json

redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

def cache_data(key, value):

    redis_client.set(
        key,
        json.dumps(value),
        ex=300
    )

def get_cached_data(key):

    data = redis_client.get(key)

    if data:
        return json.loads(data)

    return None