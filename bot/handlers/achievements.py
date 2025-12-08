from aiogram import Router, F
from aiogram.types import Message
from bot.texts import ACHIEVEMENTS
from bot.utils.user import get_user, save_user, calculate_streak

router = Router()

@router.message(F.text == "🏆 Достижения")
async def achievements(message: Message):
    user = await get_user(message.from_user.id)
    days = calculate_streak(user.start_date)
    received = user.achievements or []

    text = "🏆 ТВОИ ДОСТИЖЕНИЯ 🏆\n\n"
    for day in sorted(received):
        if day in ACHIEVEMENTS:
            a = ACHIEVEMENTS[day]
            text += f"{a['emoji']} {a['title']}\n   {a['msg']}\n\n"

    # следующее
    next_day = None
    for d in sorted(ACHIEVEMENTS.keys()):
        if d > days:
            next_day = d
            break
    if next_day:
        a = ACHIEVEMENTS[next_day]
        text += f"🎯 Следующее: {a['emoji']} {a['title']} — через {next_day - days} {streak_text(next_day - days)}"

    await message.answer(text)
