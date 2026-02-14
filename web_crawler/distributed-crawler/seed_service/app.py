from fastapi import FastAPI
import redis
import os

app = FastAPI()

redis_client = redis.Redis(host=os.getenv("REDIS_HOST"),port=6379)

@app.post("/seed")
def add_seed(url: str):
    if not redis_client.sismember("visited_urls",url):
        redis_client.lpush("url_queue",url)
    return {"message":"URL added"}