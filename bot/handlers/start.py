# bot/handlers/start.py
"""
Обработчик команды /start и кнопки '▶ Начать'
"""

import logging
from aiogram import Router, F
from aiogram.types import Message

from bot.utils.time import get_current_date
from bot.utils.user import get_user, save_user
from bot.keyboards import get_main_keyboard

logger = logging.getLogger(__name__)
router = Router()

async def start_command(message: Message):
    """Обработка команды /start"""
    chat_id = message.chat.id
    user = get_user(chat_id)
    
    # Проверяем, может пользователь уже есть?
    if user and user.get("start_date"):
        # Пользователь уже зарегистрирован
        await message.answer(
            "✨ Я уже с тобой!\n\n"
            "Используй кнопки ниже:\n"
            "• ✊ Держусь - если прямо сейчас тяжко\n"
            "• 📊 Дни - посмотреть свой прогресс\n"
            "• 🏆 Достижения - твои награды\n\n"
            "Достижения приходят автоматически в 9:00! 🎯",
            reply_markup=get_main_keyboard(),
            parse_mode="Markdown"
        )
        return
    
    # Новый пользователь
    start_date = get_current_date().isoformat()
    await save_user(chat_id, {
        "active": True,
        "start_date": start_date,
        "best_streak": 0,
        "hold_count_today": 0,
        "last_hold_date": None,
        "last_hold_time": None,
        "used_tips": [],
        "used_triggers": [],
        "used_distortions": [],
        "used_facts": [],
        "used_rage": [],
        "used_anhedonia": [],
        "achievements_received": []  # Пустой список - будут заполняться автоматически
    })
    
    await message.answer(
        "🚀 *ЧУВАКИ!*\n\n"
        "Ты начал свой путь к свободе. Каждый день в 9:00, 18:00 и 23:00 "
        "я буду присылать тебе поддержку.\n\n"
        "• ✊ Держусь - если прямо сейчас тяжко\n"
        "• 📊 Дни - посмотреть свой прогресс\n"
        "• 🏆 Достижения - твои награды\n\n"
        "🎯 *Завтра в 9:00 получишь первое достижение!*\n\n"
        "Держись, брат. Я рядом. ✊",
        reply_markup=get_main_keyboard(),
        parse_mode="Markdown"
    )
    
    logger.info(f"Новый пользователь {chat_id}, старт: {start_date}")

# Обработчик команды /start
@router.message(F.text == "/start")
async def start_command_handler(message: Message):
    await start_command(message)

# Обработчик кнопки "▶ Начать"
@router.message(F.text == "▶ Начать")
async def handle_start_button(message: Message):
    """Обработка кнопки '▶ Начать'"""
    await start_command(message)
