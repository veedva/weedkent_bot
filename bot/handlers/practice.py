from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from bot.texts import HELP_TECHNIQUES
import random

router = Router()

@router.message(F.text == "💪 Практика")
async def practice(message: Message):
    technique = random.choice(HELP_TECHNIQUES)
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="💪 Практика"), KeyboardButton(text="🧠 Информация")],
        [KeyboardButton(text="🤬 ЗЛЮСЬ"), KeyboardButton(text="💔 Срыв")],
        [KeyboardButton(text="↩ Назад")]
    ], resize_keyboard=True)
    await message.answer(technique, reply_markup=keyboard)
