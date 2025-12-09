# bot/handlers/hold.py
"""
Обработчик кнопки '✊ Держусь'
"""

import random
import asyncio
from datetime import datetime
from aiogram import Router, F
from aiogram.types import Message

from bot.utils.time import get_current_time, get_current_date
from bot.utils.user import get_user, save_user, get_active_users
from bot.texts import HOLD_RESPONSES
from bot.keyboards import get_main_keyboard

router = Router()

@router.message(F.text == "✊ Держусь")
async def handle_hold(message: Message):
    """Обработка '✊ Держусь'"""
    chat_id = message.chat.id
    user = get_user(chat_id)

    if not user.get("active", False):
        await message.answer(
            "Сначала нажми ▶ Начать",
            reply_markup=get_main_keyboard()
        )
        return

    now = get_current_time()
    today_str = now.date().isoformat()

    last_hold_date = user.get("last_hold_date")
    hold_count_today = 0
    
    if last_hold_date != today_str:
        user["last_hold_date"] = today_str
        user["hold_count_today"] = 0
    else:
        hold_count_today = user.get("hold_count_today", 0)

    last_hold_time_str = user.get("last_hold_time")
    if last_hold_time_str:
        try:
            last_time = datetime.fromisoformat(last_hold_time_str.replace("Z", "+00:00"))
            
            if (now - last_time).total_seconds() < 1800:
                await message.answer(
                    "Не надо так часто, подожди полчаса.\n"
                    "Ты молодец, что держишься.\n\n✊",
                    reply_markup=get_main_keyboard()
                )
                return
        except Exception:
            user["last_hold_time"] = None

    if hold_count_today >= 5:
        await message.answer(
            "Можно только 5 раз. Подожди до завтра.",
            reply_markup=get_main_keyboard()
        )
        return

    user["hold_count_today"] = hold_count_today + 1
    user["last_hold_time"] = now.isoformat()

    await save_user(chat_id, {
        "hold_count_today": user["hold_count_today"],
        "last_hold_time": user["last_hold_time"],
        "last_hold_date": user["last_hold_date"]
    })

    await message.answer(
        random.choice(HOLD_RESPONSES),
        reply_markup=get_main_keyboard()
    )

    # Отправляем пуш всем активным пользователям
    active_users = get_active_users()
    for uid in active_users:
        if uid != chat_id:
            try:
                await message.bot.send_message(uid, "✊")
            except Exception as e:
                error_msg = str(e).lower()
                if "blocked" in error_msg or "forbidden" in error_msg or "user is deactivated" in error_msg:
                    await save_user(uid, {"active": False})
                    # TODO: Удалить задания пользователя
