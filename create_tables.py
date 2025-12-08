from sqlalchemy.ext.asyncio import create_async_engine
from bot.config import POSTGRES_URL
from bot.models import Base
import asyncio

async def main():
    engine = create_async_engine(POSTGRES_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("Таблица users создана! Теперь всё работает навсегда ✊")

if __name__ == "__main__":
    asyncio.run(main())
