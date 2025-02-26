import importlib
redis = importlib.import_module("redis")


redis_client = redis.Redis(host="redis", port=6379, decode_responses=True)

def set_value(key: str, value: str):
    redis_client.set(key, value)

def get_value(key: str):
    return redis_client.get(key)
