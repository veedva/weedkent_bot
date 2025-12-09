# bot/keyboards.py
"""
Клавиатуры для бота
"""

from aiogram.types import (
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
    WebAppInfo
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# ========== REPLY КЛАВИАТУРЫ ==========

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Основная клавиатура"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text="✊ Держусь"),
        KeyboardButton(text="😔 Тяжело")
    )
    builder.row(
        KeyboardButton(text="👋 Ты тут?"),
        KeyboardButton(text="📊 Дни")
    )
    builder.row(
        KeyboardButton(text="❤️ Спасибо"),
        KeyboardButton(text="⏸ Помолчи")
    )
    
    return builder.as_markup(resize_keyboard=True)

def get_start_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для начала"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="▶ Начать"))
    return builder.as_markup(resize_keyboard=True)

def get_heavy_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для меню 'Тяжело'"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text="💪 Практика"),
        KeyboardButton(text="🧠 Информация")
    )
    builder.row(
        KeyboardButton(text="🤬 ЗЛЮСЬ"),
        KeyboardButton(text="💔 Срыв")
    )
    builder.row(
        KeyboardButton(text="↩ Назад")
    )
    
    return builder.as_markup(resize_keyboard=True)

def get_info_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для меню информации"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text="📅 Стадии"),
        KeyboardButton(text="🔬 Факты")
    )
    builder.row(
        KeyboardButton(text="🤯 Искажения"),
        KeyboardButton(text="⚠️ Триггеры")
    )
    builder.row(
        KeyboardButton(text="😐 Ангедония"),
        KeyboardButton(text="↩ Назад")
    )
    
    return builder.as_markup(resize_keyboard=True)

def get_days_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для меню дней"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(KeyboardButton(text="🏆 Достижения"))
    builder.row(KeyboardButton(text="↩ Назад"))
    
    return builder.as_markup(resize_keyboard=True)

# ========== INLINE КЛАВИАТУРЫ ==========

def get_exercise_keyboard(page: int = 0, total_pages: int = 22) -> InlineKeyboardMarkup:
    """Inline клавиатура для упражнений"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="◀️", callback_data="exercise_prev"),
        InlineKeyboardButton(text=f"{page+1}/{total_pages}", callback_data="exercise_page"),
        InlineKeyboardButton(text="▶️", callback_data="exercise_next")
    )
    builder.row(InlineKeyboardButton(text="✖️ Закрыть", callback_data="close_exercise"))
    
    return builder.as_markup()

def get_rage_start_keyboard() -> InlineKeyboardMarkup:
    """Начальная клавиатура для rage mode"""
    builder = InlineKeyboardBuilder()
    
    builder.row(InlineKeyboardButton(text="🤬 ДА ПИЗДЕЦ!", callback_data="rage_start_yes"))
    builder.row(InlineKeyboardButton(text="😔 Чуть-чуть", callback_data="rage_start_no"))
    builder.row(InlineKeyboardButton(text="🤷 Не знаю", callback_data="rage_start_idk"))
    builder.row(InlineKeyboardButton(text="💩 Заебало всё", callback_data="rage_start_fuckall"))
    
    return builder.as_markup()

def get_webapp_keyboard(webapp_url: str) -> InlineKeyboardMarkup:
    """Клавиатура с WebApp кнопкой"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(
            text="💥 КЛИКАЙ", 
            web_app=WebAppInfo(url=webapp_url)
        ),
        InlineKeyboardButton(
            text="✖️ Не хочу", 
            callback_data="back_from_webapp"
        )
    )
    
    return builder.as_markup()

def get_info_navigation_keyboard(
    category: str, 
    current_page: int, 
    total_pages: int
) -> InlineKeyboardMarkup:
    """Универсальная inline клавиатура для навигации"""
    builder = InlineKeyboardBuilder()
    
    builder.row(
        InlineKeyboardButton(text="◀️", callback_data=f"{category}_prev"),
        InlineKeyboardButton(text=f"{current_page}/{total_pages}", callback_data=f"{category}_page"),
        InlineKeyboardButton(text="▶️", callback_data=f"{category}_next")
    )
    builder.row(InlineKeyboardButton(text="✖️ Закрыть", callback_data="close_info"))
    
    return builder.as_markup()

# ========== УТИЛИТЫ ==========

def back_button() -> ReplyKeyboardMarkup:
    """Просто кнопка 'Назад'"""
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text="↩ Назад"))
    return builder.as_markup(resize_keyboard=True)

def simple_keyboard(buttons: list[str]) -> ReplyKeyboardMarkup:
    """Простая клавиатура из списка кнопок"""
    builder = ReplyKeyboardBuilder()
    for button in buttons:
        builder.add(KeyboardButton(text=button))
    builder.adjust(2)  # по 2 кнопки в ряд
    return builder.as_markup(resize_keyboard=True)
