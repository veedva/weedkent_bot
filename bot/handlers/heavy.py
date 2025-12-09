from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from bot.keyboards import main_keyboard, heavy_keyboard

router = Router()

@router.message(F.text == "😔 Тяжело")
async def heavy_menu(message: Message):
    await message.answer("Держись, брат. Что дальше?", reply_markup=heavy_keyboard())

@router.message(F.text == "↩ Назад")
async def back_from_heavy(message: Message):
    await message.answer("Готов дальше держать ✊", reply_markup=main_keyboard())
