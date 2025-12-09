from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

# Инлайн-меню "Тяжело"
HEAVY_MENU = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="💪 Практика", callback_data="practice")],
    [InlineKeyboardButton(text="🧠 Информация", callback_data="info_menu")],
    [InlineKeyboardButton(text="🤬 ЗЛЮСЬ", web_app=WebAppInfo(url="https://veedva.github.io/weedkent_bot/"))],
    [InlineKeyboardButton(text="💔 Срыв", callback_data="break")],
])

@router.message(F.text == "😔 Тяжело")
async def heavy_main(message: Message):
    await message.answer("Держись, брат. Что тебе нужно прямо сейчас?", reply_markup=HEAVY_MENU)

# Практика — сразу выдаёт одну технику
@router.callback_query(F.data == "practice")
async def practice_callback(call):
    from bot.texts import HELP_TECHNIQUES
    import random
    technique = random.choice(HELP_TECHNIQUES)
    await call.message.edit_text(technique, reply_markup=HEAVY_MENU)

# Меню информации
@router.callback_query(F.data == "info_menu")
async def info_menu(call):
    info_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📅 Стадии", callback_data="info_stages")],
        [InlineKeyboardButton(text="⚠️ Триггеры", callback_data="info_triggers")],
        [InlineKeyboardButton(text="🤯 Искажения", callback_data="info_distortions")],
        [InlineKeyboardButton(text="😐 Ангедония", callback_data="info_anhedonia")],
        [InlineKeyboardButton(text="🔬 Факты", callback_data="info_facts")],
        [InlineKeyboardButton(text="⬅ Назад", callback_data="heavy_main")]
    ])
    await call.message.edit_text("Что хочешь узнать?", reply_markup=info_kb)

# Все пункты информации
@router.callback_query(F.data.startswith("info_"))
async def info_detail(call):
    from bot.texts import SCIENCE_FACTS

    texts = {
        "info_stages": "1–3 дня — физическая ломка\n4–10 дней — пик тяги\n11–21 день — мозг перестраивается\n22–90 дней — восстановление рецепторов\n90+ дней — ты свободен",
        "info_triggers": "Алкоголь — главный враг\nКурение обычных сигарет — возвращает ритуал\nСтресс — 80% срывов из-за него\nСтарая компания — 95% срывов",
        "info_distortions": "Мозг будет врать:\n«Один раз не считается»\n«Только сегодня»\n«Я контролирую»\nЭто всё ложь. Ты знаешь правду.",
        "info_anhedonia": "Первые 30–60 дней — мир серый.\nЭто нормально. Рецепторы восстанавливаются.\nПосле 90 дней — цвета возвращаются.",
        "info_facts": "\n\n".join(SCIENCE_FACTS)
    }

    text = texts.get(call.data, "Нет информации")
    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="⬅ Назад в информацию", callback_data="info_menu")]
    ])
    await call.message.edit_text(text, reply_markup=back_kb)

# Возврат в главное меню "Тяжело"
@router.callback_query(F.data == "heavy_main")
async def back_to_heavy(call):
    await call.message.edit_text("Держись, брат. Что тебе нужно прямо сейчас?", reply_markup=HEAVY_MENU)

# Срыв — просто поддержка
@router.callback_query(F.data == "break")
async def break_support(call):
    await call.message.edit_text(
        "Сорвался — не конец.\n"
        "Ты всё равно дальше, чем вчера.\n"
        "Сейчас самое важное — не пойти по второму кругу.\n"
        "Просто дыши. Я рядом.",
        reply_markup=HEAVY_MENU
    )
