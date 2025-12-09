# bot/handlers/progress.py
"""
Обработчик кнопки '📊 Дни' и достижений
"""

from aiogram import Router, F
from aiogram.types import Message

from bot.utils.user import get_user
from bot.utils.time import get_days_since_start, format_days
from bot.texts import MILESTONES, ACHIEVEMENTS
from bot.keyboards import get_days_keyboard, get_main_keyboard

router = Router()

@router.message(F.text == "📊 Дни")
async def handle_days(message: Message):
    """Показать дни трезвости"""
    chat_id = message.chat.id
    user = get_user(chat_id)
    
    if not user.get("active", False):
        await message.answer(
            "Сначала нажми ▶ Начать",
            reply_markup=get_main_keyboard()
        )
        return
    
    days = get_days_since_start(user.get("start_date", ""))
    best = user.get("best_streak", 0)
    
    if days == 0:
        msg = "Ты только начинаешь. Первый день — самый важный."
    else:
        msg = f"Ты держишься {format_days(days)}."
        if best > days:
            msg += f"\n\nЛучший результат: {format_days(best)}"
        elif best > 0 and best == days:
            msg += f"\n\n⭐ Это твой лучший результат прямо сейчас!"
    
    await message.answer(msg, reply_markup=get_days_keyboard())
    
    if days in MILESTONES:
        await message.answer(
            MILESTONES[days],
            reply_markup=get_days_keyboard()
        )

@router.message(F.text == "🏆 Достижения")
async def handle_achievements(message: Message):
    """Показать достижения"""
    chat_id = message.chat.id
    user = get_user(chat_id)
    
    if not user.get("active", False):
        await message.answer(
            "Сначала нажми ▶ Начать",
            reply_markup=get_main_keyboard()
        )
        return
    
    days = get_days_since_start(user.get("start_date", ""))
    received = user.get("achievements_received", [])
    
    if not received:
        await message.answer(
            "🎯 Твои достижения появятся здесь!\n\n"
            "Продолжай держаться, и скоро здесь загорятся первые награды. 💫",
            reply_markup=get_days_keyboard()
        )
        return
    
    received_sorted = sorted(received)
    message_text = "🏆 **ТВОИ ДОСТИЖЕНИЯ** 🏆\n\n"
    
    for day_num in received_sorted:
        if day_num in ACHIEVEMENTS:
            achievement = ACHIEVEMENTS[day_num]
            message_text += f"{achievement['emoji']} **{achievement['title']}**\n"
            message_text += f"   {achievement['description']}\n"
            message_text += f"   День {day_num}\n\n"
    
    next_achievement_day = None
    for day_num in sorted(ACHIEVEMENTS.keys()):
        if day_num > days:
            next_achievement_day = day_num
            break
    
    if next_achievement_day and next_achievement_day in ACHIEVEMENTS:
        next_achievement = ACHIEVEMENTS[next_achievement_day]
        days_left = next_achievement_day - days
        message_text += f"🎯 **СЛЕДУЮЩАЯ ЦЕЛЬ:**\n"
        message_text += f"{next_achievement['emoji']} {next_achievement['title']}\n"
        message_text += f"   Осталось дней: {days_left}\n"
        message_text += f"   {next_achievement['description']}\n\n"
    
    message_text += f"📊 Всего достижений: {len(received)}/{len(ACHIEVEMENTS)}"
    
    await message.answer(
        message_text,
        reply_markup=get_days_keyboard(),
        parse_mode="Markdown"
    )
