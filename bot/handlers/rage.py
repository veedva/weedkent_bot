from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

router = Router()

@router.message(F.text == "🤬 ЗЛЮСЬ")
async def rage_mode(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(
            text="ВЗОРВАТЬ ВСЁ К ХУЯМ",
            web_app=WebAppInfo(url="https://veedva.github.io/weedkent_bot/")
        )]
    ])
    await message.answer("Слова не помогут.\nВЗРЫВАЙ.", reply_markup=keyboard)
