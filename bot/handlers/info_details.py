from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import heavy_keyboard
from bot.texts import SCIENCE_FACTS

router = Router()

# Твои оригинальные тексты — 1 в 1 из твоего файла
INFO_TEXTS = {
    "📅 Стадии": (
        "1–3 дня — физическая ломка\n"
        "4–10 дней — пик тяги\n"
        "11–21 день — мозг перестраивается\n"
        "22–90 дней — восстановление рецепторов\n"
        "90+ дней — ты свободен"
    ),
    "⚠️ Триггеры": (
        "Алкоголь — главный враг\n"
        "Курение обычных сигарет — возвращает ритуал\n"
        "Стресс — 80% срывов из-за него\n"
        "Старая компания — 95% срывов"
    ),
    "🤯 Искажения": (
        "Мозг будет врать:\n"
        "«Один раз не считается»\n"
        "«Только сегодня»\n"
        "«Я контролирую»\n"
        "Это всё ложь. Ты знаешь правду."
    ),
    "😐 Ангедония": (
        "Первые 30–60 дней — мир серый.\n"
        "Это нормально. Рецепторы восстанавливаются.\n"
        "После 90 дней — цвета возвращаются."
    ),
    "🔬 Факты": "\n\n".join(SCIENCE_FACTS)  # все 14 твоих фактов одним сообщением
}

@router.message(F.text.in_(INFO_TEXTS.keys()))
async def send_info(message: Message):
    text = INFO_TEXTS[message.text]
    await message.answer(text, reply_markup=heavy_keyboard())
