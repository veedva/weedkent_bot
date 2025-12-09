# bot/handlers/thanks.py
"""
Обработчик кнопки 'Спасибо'
"""

from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "❤️ Спасибо")
async def handle_thank_you(message: Message):
    """Поддержка проекта"""
    msg = (
        "Спасибо тебе, что ты есть. ❤️\n\n"
        "Если хочешь поддержать проект:\n"
        "Сбер: 2202 2084 3481 5313\n\n"
        "Любая сумма поможет развивать бота дальше.\n\n"
        "Главное — держись."
    )
    await message.answer(msg)
