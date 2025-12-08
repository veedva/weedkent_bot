import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import BOT_TOKEN
from bot.handlers import router

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(storage=MemoryStorage())

dp.include_router(router)

async def on_startup():
    logging.basicConfig(level=logging.INFO)
    print("@weedkent_bot — онлайн и готов держать с тобой до конца ✊")
    print("WeedKent Pro 2025 — активирован")

async def main():
    await on_startup()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
