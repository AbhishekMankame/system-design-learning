from fastapi import FastAPI
import redis
import os
app = FastAPI()
redis_client = redis.Redis(host=os.getenv("REDIS_HOST"),port=6379)

@app.get(/next)
def get_next_url():
    url=redis_client.rpop("url_queue")
    if url:
        redis_client.sadd("visited_urls",url)
        return {"url":url.decode()}
    return {"url":None}