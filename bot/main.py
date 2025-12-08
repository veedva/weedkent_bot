import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import BOT_TOKEN
from bot.handlers import router
from bot.db import create_tables  # ← важно

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)

async def on_startup():
    logging.basicConfig(level=logging.INFO)
    print("@weedkent_bot — онлайн и готов держать с тобой до конца ✊")
    print("WeedKent Pro 2025 — активирован")

async def main():
    await on_startup()
    await dp.start_polling(bot)


# 👇 временный запуск
if __name__ == "__main__":
    asyncio.run(create_tables())  # ← создает таблицы
    asyncio.run(main())           # ← запускает бота
