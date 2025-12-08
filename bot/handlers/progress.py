from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import webapp_button
from bot.utils.user import get_user, calculate_streak, streak_text

router = Router()

@router.message(F.text == "📊 Прогресс")
async def progress(message: Message):
    user = await get_user(message.from_user.id)
    if not user.active:
        await message.answer("Сначала ▶ Начать")
        return

    days = calculate_streak(user.start_date)
    best = user.best_streak or 0

    text = f"Ты держишься {streak_text(days)} 🔥\n"
    if best > days:
        text += f"Лучший результат: {streak_text(best)}\n"
    elif best == days and days > 0:
        text += "Это твой рекорд прямо сейчас!\n"

    await message.answer(text, reply_markup=webapp_button())
