# bot/handlers/practice.py
"""
Обработчик кнопки '💪 Практика' (упражнения)
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot.texts import HELP_TECHNIQUES
from bot.keyboards import get_exercise_keyboard

router = Router()

@router.message(F.text == "💪 Практика")
async def handle_exercise(message: Message):
    """Показать техники самопомощи"""
    keyboard = get_exercise_keyboard(page=0, total_pages=len(HELP_TECHNIQUES))
    
    await message.answer(
        HELP_TECHNIQUES[0],
        reply_markup=keyboard
    )

@router.callback_query(F.data.startswith("exercise_"))
async def exercise_navigation_handler(callback: CallbackQuery):
    """Навигация по упражнениям"""
    await callback.answer()
    data = callback.data
    
    if data == "close_exercise":
        await callback.message.delete()
        return
    
    current_text = callback.message.text
    
    # Находим текущий индекс
    current_index = 0
    for i, text in enumerate(HELP_TECHNIQUES):
        if text[:50] == current_text[:50]:
            current_index = i
            break
    
    if data == "exercise_next":
        new_index = (current_index + 1) % len(HELP_TECHNIQUES)
    elif data == "exercise_prev":
        new_index = (current_index - 1) % len(HELP_TECHNIQUES)
    else:
        return
    
    keyboard = get_exercise_keyboard(page=new_index, total_pages=len(HELP_TECHNIQUES))
    
    try:
        await callback.message.edit_text(
            text=HELP_TECHNIQUES[new_index],
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Ошибка навигации по упражнениям: {e}")

@router.callback_query(F.data == "close_exercise")
async def close_exercise_handler(callback: CallbackQuery):
    """Закрыть упражнение"""
    await callback.answer()
    await callback.message.delete()
