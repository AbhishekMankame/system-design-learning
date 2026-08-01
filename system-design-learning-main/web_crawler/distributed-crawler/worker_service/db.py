import asyncpg
import os

class Database:
    def __init__(self):
        self.conn = None

    async def connect(self):
        self.conn = await asyncpg.connect(
            user = "crawler",
            password = "crawler",
            database = "crawlerdb",
            host = os.getenv("POSTGRES_HOST","localhost")
        )

    async def save_page(self, url:str, content: str):
        await self.conn.execute(
            """ 
            INSERT INTO pages (url, content)
            VALUES ($1, $2)
            ON CONFLICT (url) DO NOTHING
            """,
            url,
            content
        )