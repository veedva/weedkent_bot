from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "❤️ Спасибо")
async def thanks(message: Message):
    await message.answer(
        "Спасибо тебе, брат ❤️\n\n"
        "Если хочешь поддержать:\n"
        "Сбер: 2202 2084 3481 5313\n\n"
        "Любая сумма — это топливо для бота."
    )
