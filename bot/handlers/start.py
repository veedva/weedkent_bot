from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from bot.keyboards import main_keyboard, start_keyboard
from bot.utils.user import get_user, save_user, schedule_jobs
from bot.utils.time import today

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    user = await get_user(message.from_user.id)
    if user.active:
        await message.answer(
            f"С возвращением, брат. Ты держишься {user.streak} {user.streak_text}.\nЯ рядом.",
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

    # заполняем поля пользователя
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
