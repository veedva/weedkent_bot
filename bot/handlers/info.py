from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text == "🧠 Информация")
async def info_menu(message: Message):
    await message.answer(
        "Выбери:\n\n"
        "📅 Стадии\n"
        "⚠️ Триггеры\n"
        "🤯 Искажения\n"
        "😐 Ангедония\n"
        "🔬 Факты",
        reply_markup=get_info_keyboard()
    )
