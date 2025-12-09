# bot/handlers/info.py
"""
Обработчик информационных разделов (стадии, триггеры, искажения и т.д.)
"""

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from bot.texts import (
    RECOVERY_STAGES, 
    TRIGGERS_INFO, 
    COGNITIVE_DISTORTIONS,
    ANHEDONIA_INFO, 
    SCIENCE_FACTS
)
from bot.keyboards import get_info_navigation_keyboard

router = Router()

@router.message(F.text == "📅 Стадии")
async def handle_stages(message: Message):
    """Стадии восстановления"""
    keyboard = get_info_navigation_keyboard(
        category="stages",
        current_page=1,
        total_pages=len(RECOVERY_STAGES)
    )
    
    await message.answer(
        RECOVERY_STAGES[0],
        reply_markup=keyboard
    )

@router.message(F.text == "⚠️ Триггеры")
async def handle_triggers(message: Message):
    """Триггеры"""
    keyboard = get_info_navigation_keyboard(
        category="triggers",
        current_page=1,
        total_pages=len(TRIGGERS_INFO)
    )
    
    await message.answer(
        TRIGGERS_INFO[0],
        reply_markup=keyboard
    )

@router.message(F.text == "🤯 Искажения")
async def handle_distortions(message: Message):
    """Когнитивные искажения"""
    keyboard = get_info_navigation_keyboard(
        category="distortions",
        current_page=1,
        total_pages=len(COGNITIVE_DISTORTIONS)
    )
    
    await message.answer(
        COGNITIVE_DISTORTIONS[0],
        reply_markup=keyboard
    )

@router.message(F.text == "😐 Ангедония")
async def handle_anhedonia(message: Message):
    """Ангедония"""
    keyboard = get_info_navigation_keyboard(
        category="anhedonia",
        current_page=1,
        total_pages=len(ANHEDONIA_INFO)
    )
    
    await message.answer(
        ANHEDONIA_INFO[0],
        reply_markup=keyboard
    )

@router.message(F.text == "🔬 Факты")
async def handle_facts(message: Message):
    """Научные факты"""
    keyboard = get_info_navigation_keyboard(
        category="facts",
        current_page=1,
        total_pages=len(SCIENCE_FACTS)
    )
    
    await message.answer(
        SCIENCE_FACTS[0],
        reply_markup=keyboard
    )

@router.callback_query(F.data.startswith(("stages_", "triggers_", "distortions_", "anhedonia_", "facts_")))
async def info_navigation_handler(callback: CallbackQuery):
    """Навигация по информационным разделам"""
    await callback.answer()
    
    data = callback.data
    
    if data == "close_info":
        await callback.message.delete()
        return
    
    # Определяем какой раздел
    if data.startswith("stages_"):
        info_list = RECOVERY_STAGES
        category = "stages"
    elif data.startswith("triggers_"):
        info_list = TRIGGERS_INFO
        category = "triggers"
    elif data.startswith("distortions_"):
        info_list = COGNITIVE_DISTORTIONS
        category = "distortions"
    elif data.startswith("anhedonia_"):
        info_list = ANHEDONIA_INFO
        category = "anhedonia"
    elif data.startswith("facts_"):
        info_list = SCIENCE_FACTS
        category = "facts"
    else:
        return
    
    current_text = callback.message.text
    
    # Находим текущий индекс
    current_index = 0
    for i, text in enumerate(info_list):
        if text[:50] == current_text[:50]:
            current_index = i
            break
    
    if data.endswith("_next"):
        new_index = (current_index + 1) % len(info_list)
    elif data.endswith("_prev"):
        new_index = (current_index - 1) % len(info_list)
    else:
        return
    
    keyboard = get_info_navigation_keyboard(
        category=category,
        current_page=new_index + 1,
        total_pages=len(info_list)
    )
    
    try:
        await callback.message.edit_text(
            text=info_list[new_index],
            reply_markup=keyboard
        )
    except Exception as e:
        print(f"Ошибка навигации по {category}: {e}")

@router.callback_query(F.data == "close_info")
async def close_info_handler(callback: CallbackQuery):
    """Закрыть информационное сообщение"""
    await callback.answer()
    await callback.message.delete()
