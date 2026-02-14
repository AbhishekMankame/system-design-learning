import asyncio
import aiohttp
import redis
import os
from bs4 import BeautifulSoup
from db import Database
from shared.config import *

redis_client = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379)

db = Database()

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            return await response.text()
    except:
        return None

def extract_links(html):
    soup = BeautifulSoup(html, "html.parser")
    return [a.get("href") for a in soup.find_all("a", href=True)]

async def worker():
    await db.connect()   # 🔥 connect once

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

            # ✅ Save to DB
            await db.save_page(url, html)

            # Extract and enqueue new URLs
            links = extract_links(html)
            for link in links:
                if not redis_client.sismember(VISITED_SET, link):
                    redis_client.lpush(QUEUE_NAME, link)

            await asyncio.sleep(CRAWL_DELAY)

asyncio.run(worker())
