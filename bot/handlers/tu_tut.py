from aiogram import Router, F
from aiogram.types import Message
import asyncio
import random

router = Router()

TU_TUT_FIRST = ["Тут.", "Привет.", "А куда я денусь?", "Здесь.", "Да, брат."]
TU_TUT_SECOND = ["Держись, я рядом.", "Я с тобой.", "Всё будет.", "Не сдавайся ✊"]

@router.message(F.text == "👋 Ты тут?")
async def tu_tut(message: Message):
    await asyncio.sleep(random.randint(2, 6))
    await message.answer(random.choice(TU_TUT_FIRST))
    await asyncio.sleep(random.randint(2, 5))
    await message.answer(random.choice(TU_TUT_SECOND))
