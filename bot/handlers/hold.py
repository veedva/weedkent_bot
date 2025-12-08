from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import main_keyboard
from bot.utils.user import get_user, save_user
from bot.utils.time import now, today
import random

router = Router()

HOLD_RESPONSES = ["Понял.", "Молодец.", "Так держать.", "Отправлено.", "Красавчик."]

@router.message(F.text == "✊ Держусь")
async def hold(message: Message):
    user = await get_user(message.from_user.id)
    
    if not user.active:
        await message.answer("Сначала ▶ Начать")
        return

    today_date = today()
    
    # Сброс счётчика, если новый день
    if not user.last_hold_date or user.last_hold_date != today_date:
        user.hold_count_today = 0
        user.last_hold_date = today_date

    # лимит 5 раз в день + не чаще 30 минут
    if user.hold_count_today >= 5:
        await message.answer("Только 5 раз в день, брат. Завтра снова можно.")
        return

    if user.last_hold_time:
        delta = now() - user.last_hold_time
        if delta.total_seconds() < 1800:
            await message.answer("Не чаще чем раз в полчаса. Ты и так молодец ✊")
            return

    # обновляем данные пользователя
    user.hold_count_today += 1
    user.last_hold_time = now()

    await save_user(user)

    await message.answer(random.choice(HOLD_RESPONSES), reply_markup=main_keyboard())

    # временный пуш самому себе
    await message.bot.send_message(message.from_user.id, "✊")
