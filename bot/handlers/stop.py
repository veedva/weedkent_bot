from aiogram import Router, F
from aiogram.types import Message
from bot.utils.user import get_user, save_user

router = Router()

@router.message(F.text == "⏸ Помолчи")
async def stop(message: Message):
    user = await get_user(message.from_user.id)
    user.active = False
    await save_user(user)
    await message.answer("Рассылки остановлены. Возвращайся, когда готов ✊")
