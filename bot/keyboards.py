from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

def main_keyboard():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="✊ Держусь"), KeyboardButton(text="😔 Тяжело")],
        [KeyboardButton(text="📊 Прогресс"), KeyboardButton(text="👋 Ты тут?")],
        [KeyboardButton(text="❤️ Спасибо"), KeyboardButton(text="⏸ Помолчи")]
    ], resize_keyboard=True)

def heavy_keyboard():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="💪 Практика"), KeyboardButton(text="🧠 Информация")],
        [KeyboardButton(text="🤬 ЗЛЮСЬ"), KeyboardButton(text="💔 Срыв")],
        [KeyboardButton(text="↩ Назад")]
    ], resize_keyboard=True)

# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
# ЭТОЙ КНОПКИ НЕ БЫЛО — Я ДОБАВЛЯЮ
def start_keyboard():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="▶ Начать")]
    ], resize_keyboard=True)
# ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
