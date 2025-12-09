from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(F.text == "🧠 Информация")
async def info_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="📅 Стадии"), KeyboardButton(text="⚠️ Триггеры")],
        [KeyboardButton(text="🤯 Искажения"), KeyboardButton(text="😐 Ангедония")],
        [KeyboardButton(text="🔬 Факты"), KeyboardButton(text="↩ Назад")]
    ], resize_keyboard=True)
    await message.answer(
        "Что хочешь узнать?",
        reply_markup=keyboard
    )
