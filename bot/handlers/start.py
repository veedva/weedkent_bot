# bot/handlers/start.py - УПРОЩЁННАЯ ВЕРСИЯ
"""
Упрощённый обработчик команды /start для тестирования
"""

import logging
from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from bot.utils.time import get_current_date
from bot.utils.user import get_user, save_user
from bot.keyboards import get_main_keyboard

logger = logging.getLogger(__name__)
router = Router()

@router.message(Command("start"))
async def start_command(message: Message):
    """Простая версия /start для тестирования"""
    chat_id = message.chat.id
    
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
