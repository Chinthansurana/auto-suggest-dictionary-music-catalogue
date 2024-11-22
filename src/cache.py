import redis

def setup_redis(redis_host='localhost', redis_port=6379):
    return redis.StrictRedis(host=redis_host, port=redis_port, db=0)

def cache_prefix(redis_client, prefix, suggestions):
    redis_client.set(f'prefix:{prefix}', ','.join(suggestions))

def get_cached_prefix(redis_client, prefix):
    cached = redis_client.get(f'prefix:{prefix}')
    if cached:
        return cached.decode('utf-8').split(',')
    return None
