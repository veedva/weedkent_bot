from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

def main_keyboard():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="✊ Держусь"), KeyboardButton(text="😔 Тяжело")],
        [KeyboardButton(text="📊 Прогресс"), KeyboardButton(text="👋 Ты тут?")],
        [KeyboardButton(text="❤️ Спасибо"), KeyboardButton(text="⏸ Помолчи")]
    ], resize_keyboard=True)

def heavy_keyboard():
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Практика"), KeyboardButton(text="Информация")],
        [KeyboardButton(text="ЗЛЮСЬ"), KeyboardButton(text="Срыв")],
        [KeyboardButton(text="↩ Назад")]
    ], resize_keyboard=True)

def webapp_button():
    # Сюда потом вставишь свой настоящий URL после деплоя Mini App
    return ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Мой прогресс", web_app=WebAppInfo(url="https://durachok-pro.up.railway.app"))],
        [KeyboardButton(text="↩ Назад")]
    ], resize_keyboard=True)
