# bot/handlers/start.py
"""
Обработчик команды /start и кнопки '▶ Начать'
"""

import logging
from aiogram import Router, F
from aiogram.types import Message

from bot.utils.time import get_current_date
from bot.utils.user import get_user, save_user, check_and_give_achievements
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
    
    # Проверяем и выдаём достижения
    new_achievements = await check_and_give_achievements(chat_id)
    
    await message.answer(
        "🚀 *ЧУВАКИ!*\n\n"
        "Это тестовая версия с новой архитектурой.\n"
        "Основной бот продолжает работать как обычно.\n\n"
        "Держись, брат. Я рядом. ✊",
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown"
    )
    
    # Выдаём достижения если есть
    if new_achievements:
        for day_num, achievement in new_achievements:
            await message.answer(
                f"{achievement['emoji']} **НОВОЕ ДОСТИЖЕНИЕ!** {achievement['emoji']}\n\n"
                f"**{achievement['title']}**\n"
                f"{achievement['description']}\n\n"
                f"{achievement['message']}\n\n"
                f"🎯 День: {day_num}",
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
