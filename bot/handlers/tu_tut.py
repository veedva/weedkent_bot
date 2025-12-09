from aiogram import Router, F
from aiogram.types import Message
import asyncio
import random

router = Router()

TU_TUT = ["Тут.", "Привет.", "Ага.", "Здесь.", "Да, брат."]

@router.message(F.text == "👋 Ты тут?")
async def tu_tut(message: Message):
    await asyncio.sleep(random.randint(2, 5))
    await message.answer(random.choice(TU_TUT))
    await asyncio.sleep(random.randint(2, 4))
    await message.answer("Держись ✊")
