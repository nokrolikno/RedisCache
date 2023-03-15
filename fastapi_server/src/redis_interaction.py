import redis

r = redis.Redis(host='redis', port=6999)


def r_get(key: str) -> str:
    return r.get(key)


def r_set(key: str, value: str) -> bool:
    return r.set(key, value)
