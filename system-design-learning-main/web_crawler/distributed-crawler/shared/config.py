import os

REDIS_HOST = os.getenv("REDIS_HOST","localhost")
POSTGRES_HOST = os.getenv("POSTGRES_HOST","localhost")

QUEUE_NAME = "url_queue"
VISITED_SET = "visited_urls"

CRAWL_DELAY = 1