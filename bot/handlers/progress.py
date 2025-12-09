from aiogram import Router, F
from aiogram.types import Message, WebAppInfo
from bot.keyboards import main_keyboard
from bot.utils.user import get_user, calculate_streak, streak_text

router = Router()

@router.message(F.text == "📊 Прогресс")
async def show_progress(message: Message):
    user = await get_user(message.from_user.id)
    
    if not user.active:
        await message.answer("Сначала жми ▶ Начать, брат.")
        return

    days = calculate_streak(user.start_date)
    best = user.best_streak or 0

    text = f"🔥 Ты держишься {streak_text(days)}\n"
    if best > days:
        text += f"Лучший результат: {streak_text(best)}\n"
    elif best == days and days > 0:
        text += "Это твой рекорд прямо сейчас!\n"

    text += "\nЖми кнопку ниже — увидишь график дофамина, ачивки и прогноз."

    keyboard = [
        [Message.button.web_app(
            text="🌿 Мой прогресс",
            web_app=WebAppInfo(url="https://veedva.github.io/weedkent_bot/webapp/")
        )],
        [Message.button.text("↩ Назад")]
    ]

    await message.answer(
        text,
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    )
