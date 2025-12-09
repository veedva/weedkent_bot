# bot/handlers/heavy.py
"""
Обработчик кнопки '😔 Тяжело' и подменю
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.keyboards import get_heavy_keyboard, get_info_keyboard, get_main_keyboard, get_start_keyboard
from bot.utils.user import reset_user_progress, get_user_days

router = Router()

@router.message(F.text == "😔 Тяжело")
async def handle_heavy(message: Message):
    """Обработка '😔 Тяжело'"""
    await message.answer(
        "Понимаю, бывает тяжело.\n\n"
        "Выбери, что нужно прямо сейчас:\n\n"
        "💪 Практика — быстрые техники самопомощи\n"
        "🧠 Информация — научные факты и методы\n"
        "🤬 ЗЛЮСЬ — rage mode\n"
        "💔 Срыв — сбрасывает прогресс\n\n"
        "Помни, это пройдёт. Всегда проходит.",
        reply_markup=get_heavy_keyboard()
    )

@router.message(F.text == "🧠 Информация")
async def handle_info_menu(message: Message):
    """Меню информации"""
    await message.answer(
        "Выбери раздел:\n\n"
        "📅 Стадии — что происходит с тобой\n"
        "⚠️ Триггеры — что вызывает тягу и как бороться\n"
        "🤯 Искажения — ошибки мышления\n"
        "😐 Ангедония — когда ничего не радует\n"
        "🔬 Факты — научные факты о восстановлении",
        reply_markup=get_info_keyboard()
    )

@router.message(F.text == "↩ Назад")
async def handle_back(message: Message):
    """Вернуться назад"""
    await message.answer("Окей", reply_markup=get_main_keyboard())

@router.message(F.text == "💔 Срыв")
async def handle_breakdown(message: Message):
    """Сброс прогресса при срыве"""
    chat_id = message.chat.id
    
    # Подтверждение с инлайн-кнопками
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="✅ ДА, сбросить", callback_data="reset_confirm"),
        InlineKeyboardButton(text="❌ НЕТ, передумал", callback_data="reset_cancel")
    )
    
    await message.answer(
        "⚠️ *ТОЧНО СБРОСИТЬ ПРОГРЕСС?*\n\n"
        "Это обнулит твой счётчик дней, достижения и всю статистику.\n"
        "Лучший результат сохранится.\n\n"
        "Это необратимо. Ты уверен?",
        reply_markup=builder.as_markup(),
        parse_mode="Markdown"
    )

@router.callback_query(F.data == "reset_confirm")
async def handle_reset_confirm(callback: CallbackQuery):
    """Подтверждение сброса прогресса"""
    await callback.answer()
    
    chat_id = callback.message.chat.id
    
    # Получаем сколько дней было
    days_lost = get_user_days(chat_id)
    
    # Сбрасываем прогресс
    await reset_user_progress(chat_id)
    
    # Удаляем сообщение с кнопками
    await callback.message.delete()
    
    # Отправляем финальное сообщение
    await callback.message.answer(
        f"💔 *Счётчик сброшен*\n\n"
        f"Ты продержался {days_lost} {'день' if days_lost == 1 else 'дней'}.\n\n"
        f"Это не провал. Это данные для следующей попытки.\n\n"
        f"Когда будешь готов начать снова — жми ▶ Начать",
        reply_markup=get_start_keyboard(),
        parse_mode="Markdown"
    )

@router.callback_query(F.data == "reset_cancel")
async def handle_reset_cancel(callback: CallbackQuery):
    """Отмена сброса прогресса"""
    await callback.answer("Отменено")
    await callback.message.delete()
    await callback.message.answer(
        "Хорошее решение. Продолжай держаться! ✊",
        reply_markup=get_heavy_keyboard()
    )
