from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import heavy_keyboard, main_keyboard
from bot.texts import HELP_TECHNIQUES
import random

router = Router()

@router.message(F.text == "💪 Практика")
async def practice(message: Message):
    technique = random.choice(HELP_TECHNIQUES)
    await message.answer(technique, reply_markup=heavy_keyboard())
