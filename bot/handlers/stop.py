# bot/handlers/stop.py
"""
Обработчик команды /stop и кнопки '⏸ Помолчи'
"""

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from bot.utils.user import save_user
from bot.keyboards import get_start_keyboard

router = Router()

@router.message(Command("stop"))
@router.message(F.text == "⏸ Помолчи")
async def stop_command(message: Message):
    """Остановить уведомления"""
    chat_id = message.chat.id
    
    await save_user(chat_id, {"active": False})
    
    await message.answer(
        "Уведомления остановлены.\nКогда будешь готов — жми ▶ Начать",
        reply_markup=get_start_keyboard()
    )
