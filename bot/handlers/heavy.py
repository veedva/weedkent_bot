from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

router = Router()

@router.message(F.text == "😔 Тяжело")
async def heavy_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="💪 Практика"), KeyboardButton(text="🧠 Информация")],
        [KeyboardButton(text="🤬 ЗЛЮСЬ"), KeyboardButton(text="💔 Срыв")],
        [KeyboardButton(text="↩ Назад")]
    ], resize_keyboard=True)
    await message.answer("Держись, брат. Что дальше?", reply_markup=keyboard)
