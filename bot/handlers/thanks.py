from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "❤️ Спасибо")
async def thanks(message: Message):
    await message.answer("Спасибо тебе, брат ❤️\n\nЕсли хочешь поддержать:\nСбер 2202 2084 3481 5313\n\nЛюбая сумма поможет.")
