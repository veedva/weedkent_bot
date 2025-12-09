# bot/handlers/rage.py
"""
Обработчик rage mode
"""

import random
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.texts import RAGE_TECHNIQUES
from bot.keyboards import get_heavy_keyboard, get_webapp_keyboard, get_rage_start_keyboard
from bot.config import KATHARSIS_WEBAPP_URL

router = Router()

@router.message(F.text == "🤬 ЗЛЮСЬ")
async def handle_rage(message: Message):
    """Rage mode с WebApp кликером"""
    chat_id = message.chat.id
    
    # 33% - WebApp кликер, 33% - опросник, 33% - текстовая техника
    choice = random.choice(["webapp", "questionnaire", "text"])
    
    if choice == "webapp":
        keyboard = get_webapp_keyboard(KATHARSIS_WEBAPP_URL)
        
        await message.answer(
            "💢 *Слова не помогут.*\n\n"
            "Время действовать.",
            reply_markup=keyboard,
            parse_mode="Markdown"
        )
        return
    
    elif choice == "questionnaire":
        keyboard = get_rage_start_keyboard()
        await message.answer("Чё, жопа горит?", reply_markup=keyboard)
    
    else:  # choice == "text"
        # Простая текстовая техника (пока без сохранения использованных)
        rage = random.choice(RAGE_TECHNIQUES)
        await message.answer(rage, reply_markup=get_heavy_keyboard())

@router.callback_query(F.data.startswith("rage_"))
async def rage_callback_handler(callback: CallbackQuery):
    """Обработчик rage callback"""
    await callback.answer()
    data = callback.data
    
    final_responses = {
        "rage_self": "Не ругай себя. Ты всё ещё здесь — это уже победа. ✊",
        "rage_people": "Люди — уёбки. Многие просто не понимают. Это не твоя вина. Иди дальше, брат.",
        "rage_world": "Мир — жесток. Но ты сильнее его. Пусть идёт нахуй.",
        "rage_ex": "Да, именно этот человек сейчас как нож в спину. Проживи эту боль трезвым — она уйдёт быстрее.",
        
        "rage_anxiety": "Тревога орёт, что всё пропало. Она врёт. Это химия. Через 15 минут легче. Дыши 4-7-8.",
        "rage_sad": "Сейчас кажется, что ничего хорошего больше не будет. Это ложь ангедония. Через 10–14 дней отпустит.",
        "rage_empty": "Пусто внутри — дофамина ноль. Это не ты, это мозг учится жить без химии. Держись до первых искр.",
        
        "rage_chest": "В груди огонь? 20 отжиманий до дрожи или лёд на шею 60 сек. Сбросишь физически — отпустит.",
        "rage_head": "Мысли как тараканы. Назови вслух 5 предметов вокруг. Ещё 5. Возвращает в тело.",
        "rage_body": "Тело ломает? Потряси руками-ногами как собака после дождя 30 сек. Смешно, но работает.",
        
        "rage_fuck_self": "Ты не заебал. Ты устал быть рабом вещества. Это последний бой. Ты почти выиграл.",
        "rage_fuck_people": "Пусть идут нахуй. Сейчас твоя задача — спасти себя.",
        "rage_fuck_time": "Первый месяц время как говно. Это мозг перезагружается. Скоро пролетит незаметно.",
        "rage_fuck_everything": "Когда всё хуйня — остаётся одно: просто быть. И этого достаточно.",
    }

    if data == "rage_calm":
        await callback.message.delete()
        await callback.message.answer(
            "Все будет хорошо, расслабься.",
            reply_markup=get_heavy_keyboard()
        )
        return

    if data == "rage_restart":
        keyboard = get_rage_start_keyboard()
        await callback.message.edit_text("Ладно, ещё раз. Че, злишься?", reply_markup=keyboard)
        return

    if data == "rage_start_yes":
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text="😞 На себя", callback_data="rage_self"),
            InlineKeyboardButton(text="👥 На людей", callback_data="rage_people")
        )
        builder.row(
            InlineKeyboardButton(text="🌍 На весь мир", callback_data="rage_world"),
            InlineKeyboardButton(text="💔 На неё/него", callback_data="rage_ex")
        )
        await callback.message.edit_text("На кого или на что конкретно?", reply_markup=builder.as_markup())

    elif data == "rage_start_no":
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text="😰 Тревога 100/100", callback_data="rage_anxiety"))
        builder.row(InlineKeyboardButton(text="😭 Грусть/тоска", callback_data="rage_sad"))
        builder.row(InlineKeyboardButton(text="🗑 Пустота внутри", callback_data="rage_empty"))
        await callback.message.edit_text("Что конкретно жрёт изнутри?", reply_markup=builder.as_markup())

    elif data == "rage_start_idk":
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text="🔥 В груди как огонь", callback_data="rage_chest"))
        builder.row(InlineKeyboardButton(text="🤯 В голове каша", callback_data="rage_head"))
        builder.row(InlineKeyboardButton(text="💀 Во всём теле ломает", callback_data="rage_body"))
        await callback.message.edit_text("Где конкретно плохо?", reply_markup=builder.as_markup())

    elif data == "rage_start_fuckall":
        builder = InlineKeyboardBuilder()
        builder.row(InlineKeyboardButton(text="😔 Я сам себя заебал", callback_data="rage_fuck_self"))
        builder.row(InlineKeyboardButton(text="🧑‍🤝‍🧑 Все вокруг", callback_data="rage_fuck_people"))
        builder.row(InlineKeyboardButton(text="⏰ Время тянется как говно", callback_data="rage_fuck_time"))
        builder.row(InlineKeyboardButton(text="🌪 Всё это вообще", callback_data="rage_fuck_everything"))
        await callback.message.edit_text("Что больше всего заебало?", reply_markup=builder.as_markup())

    elif data in final_responses:
        builder = InlineKeyboardBuilder()
        builder.row(
            InlineKeyboardButton(text="🔥 ЕЩЁ РАЗ!", callback_data="rage_restart"),
            InlineKeyboardButton(text="🧘🏻 Вроде отпустило", callback_data="rage_calm")
        )
        text = f"{final_responses[data]}\n\nДержись, брат. Это пройдёт."
        await callback.message.edit_text(text, reply_markup=builder.as_markup())

@router.callback_query(F.data == "back_from_webapp")
async def back_from_webapp_callback(callback: CallbackQuery):
    """Обработчик кнопки 'Назад' после WebApp"""
    await callback.answer()
    await callback.message.delete()
