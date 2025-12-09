# bot/handlers/heavy.py
"""
Обработчик кнопки '😔 Тяжело' и подменю
"""

from aiogram import Router, F
from aiogram.types import Message

from bot.keyboards import get_heavy_keyboard, get_info_keyboard, get_main_keyboard

router = Router()

@router.message(F.text == "😔 Тяжело")
async def handle_heavy(message: Message):
    """Обработка '😔 Тяжело'"""
    await message.answer(
        "Понимаю, бывает тяжело.\n\n"
        "Выбери, что нужно прямо сейчас:\n\n"
        "💪 Практика — быстрые техники самопомощи\n"
        "🧠 Информация — научные факты и методы\n"
        "🤬 ЗЛЮСЬ — rage mode\n"
        "💔 Срыв — сбрасывает прогресс\n\n"
        "Помни, это пройдёт. Всегда проходит.",
        reply_markup=get_heavy_keyboard()
    )

@router.message(F.text == "🧠 Информация")
async def handle_info_menu(message: Message):
    """Меню информации"""
    await message.answer(
        "Выбери раздел:\n\n"
        "📅 Стадии — что происходит с тобой\n"
        "⚠️ Триггеры — что вызывает тягу и как бороться\n"
        "🤯 Искажения — ошибки мышления\n"
        "😐 Ангедония — когда ничего не радует\n"
        "🔬 Факты — научные факты о восстановлении",
        reply_markup=get_info_keyboard()
    )

@router.message(F.text == "↩ Назад")
async def handle_back(message: Message):
    """Вернуться назад"""
    await message.answer("Окей", reply_markup=get_main_keyboard())
