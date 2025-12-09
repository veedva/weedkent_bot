# bot/handlers/start.py
"""
Обработчик команды /start и кнопки '▶ Начать'
"""

import logging
from aiogram import Router, F
from aiogram.types import Message

from bot.utils.time import get_current_date
from bot.utils.user import get_user, save_user
from bot.keyboards import get_main_keyboard, get_start_keyboard

logger = logging.getLogger(__name__)
router = Router()

async def start_command(message: Message):
    """Обработка команды /start"""
    chat_id = message.chat.id
    user = get_user(chat_id)
    
    # Простая версия для тестов
    await save_user(chat_id, {
        "active": True,
        "start_date": get_current_date().isoformat(),
        "hold_count_today": 0,
    })
    
    await message.answer(
        "🚀 *ТЕСТОВЫЙ БОТ ЗАПУЩЕН!*\n\n"
        "Это тестовая версия с новой архитектурой.\n"
        "Основной бот продолжает работать как обычно.\n\n"
        "Команда /test - проверить работу\n"
        "Команда /debug - отладочная информация",
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown"
    )
    
    logger.info(f"Тестовый /start от {chat_id}")

# Обработчик команды /start
@router.message(F.text == "/start")
async def start_command_handler(message: Message):
    await start_command(message)

# Обработчик кнопки "▶ Начать"
@router.message(F.text == "▶ Начать")
async def handle_start_button(message: Message):
    """Обработка кнопки '▶ Начать'"""
    await start_command(message)
