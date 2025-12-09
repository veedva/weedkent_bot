# bot/handlers/tu_tut.py
"""
Обработчик кнопки 'Ты тут?'
"""

import random
import asyncio
from aiogram import Router, F
from aiogram.types import Message

from bot.texts import TU_TUT_FIRST, TU_TUT_SECOND

router = Router()

@router.message(F.text == "👋 Ты тут?")
async def handle_are_you_here(message: Message):
    """Проверка работы бота"""
    await asyncio.sleep(random.randint(2, 6))
    await message.answer(random.choice(TU_TUT_FIRST))
    
    await asyncio.sleep(random.randint(2, 5))
    await message.answer(random.choice(TU_TUT_SECOND))
