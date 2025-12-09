import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import BOT_TOKEN
from bot.handlers import router
from bot.jobs import start_scheduler

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# ВРЕМЕННЫЙ БЛОК — создаёт таблицу при старте
from sqlalchemy.ext.asyncio import create_async_engine
from bot.models import Base
from bot.config import DATABASE_URL

async def create_tables():
    engine = create_async_engine(DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"))
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await engine.dispose()
    print("Таблица users создана навсегда ✊")
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←

logging.basicConfig(level=logging.INFO)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)

async def on_startup():
    print("@weedkent_bot — онлайн и готов держать с тобой до конца ✊")
    print("WeedKent Pro 2025 — активирован")
    await start_scheduler(bot)

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    # ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
    # Один раз создаст таблицу, потом можно удалить эти строки
    asyncio.run(create_tables())
    # ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
    asyncio.run(main())
