import asyncio
import aiohttp
import redis
import os
import asyncpg
from bs4 import BeautifulSoup
from shared.config import *

redis client = redis.Redis(host=os.getenv("REDIS_HOST"),post=6379)

async def fetch(session,url):
    try:
        async with session.get(url,timeout=10) as response:
            return await response.text()
    except:
        return None

async def save_to_db(conn,url,content):
    await conn.execute(
        "INSERT INTO pages(url,content) VALUES($1,$2)",
        url, content
    )

async def extract_links(html, base_url):
    soup = BeautifulSoup(html, "html.parser")
    return [a.get("href") for a in soup.find_all("a",href=True)]

async def worker():
    conn = await asyncpg.connect(
        user="crawler",
        password="crawler",
        database="crawlerdb",
        host=os.getenv("POSTGRES_HOST")
    )

    async with aiohttp.ClientSession() as session:
        while True:
            url = redis_client.rpop(QUEUE_NAME)
            if not url:
                await asyncio.sleep(1)
                continue

            url = url.decode()

            html = await fetch(session, url)
            if not html:
                continue

            await save_to_db(conn, url, html)

            links = await extract_links(html, url)
            for link in links:
                if not redis_client.sismember(VISITED_SET, link):
                    redis_client.lpush(QUEUE_NAME, link)

            await asyncio.sleep(CRAWL_DELAY)

asyncio.run(worker())