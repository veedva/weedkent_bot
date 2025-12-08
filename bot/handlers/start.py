from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards import main_keyboard, start_keyboard
from bot.utils.user import get_user, save_user, schedule_jobs
from bot.utils.time import today

router = Router()

def calculate_streak(user) -> int:
    if not user.start_date:
        return 0
    delta = today() - user.start_date
    return max(delta.days + 1, 0)  # День 1 считается первым днём

def streak_text(days: int) -> str:
    if days == 0:
        return "0 дней"
    if 11 <= days % 100 <= 19:
        return f"{days} дней"
    if days % 10 == 1:
        return f"{days} день"
    if days % 10 in (2, 3, 4):
        return f"{days} дня"
    return f"{days} дней"

@router.message(Command("start"))
async def cmd_start(message: Message):
    user = await get_user(message.from_user.id)
    
    if user.active:
        streak = calculate_streak(user)
        text = streak_text(streak)
        await message.answer(
            f"С возвращением, брат. Ты держишься {streak} {text}.\nЯ рядом.",
            reply_markup=main_keyboard()
        )
    else:
        await message.answer(
            "Привет, брат 👋\n\n"
            "Я — Дурачок Pro. Буду писать тебе 3 раза в день — просто чтобы напомнить: сегодня не стоит.\n\n"
            "Когда тяжело — жми ✊ Держусь\n"
            "Можно до 5 раз в день.\n\n"
            "Готов начать?",
            reply_markup=start_keyboard()
        )

@router.message(F.text == "▶ Начать")
async def real_start(message: Message):
    user = await get_user(message.from_user.id)
    
    if user.active:
        await message.answer("Ты уже в деле, брат.")
        return

    # активируем пользователя
    user.active = True
    user.start_date = today()
    user.achievements = []
    user.mood_history = []

    await save_user(user)
    await schedule_jobs(message.from_user.id, message.bot)

    await message.answer(
        "Поехали. День 1 начался.\n\nДержись, я рядом ✊",
        reply_markup=main_keyboard()
    )
