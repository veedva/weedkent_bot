from sqlalchemy.ext.asyncio import create_async_engine
from bot.config import POSTGRES_URL
from bot.models import Base
import asyncio

async def create_tables():
    engine = create_async_engine(POSTGRES_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("Таблица users создана успешно!")

if __name__ == "__main__":
    asyncio.run(create_tables())
