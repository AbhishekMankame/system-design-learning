import os

# ------------------------------
# Redis configuration
# ------------------------------
REDIS_HOST = os.getenv("REDIS_HOST", "redis")   # Docker service name for Redis
QUEUE_NAME = "url_queue"                        # Redis list for URLs
VISITED_SET = "visited_urls"                    # Redis set for deduplication

# ------------------------------
# Crawl settings
# ------------------------------
CRAWL_DELAY = 1                                 # Seconds to wait between fetches

# ------------------------------
# Postgres configuration
# ------------------------------
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")  # Docker service name for Postgres
POSTGRES_USER = "crawler"
POSTGRES_PASSWORD = "crawler"
POSTGRES_DB = "crawlerdb"
POSTGRES_PORT = 5432
