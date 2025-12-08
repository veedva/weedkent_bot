from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from bot.texts import RAGE_RESPONSES

router = Router()

@router.message(F.text == "ЗЛЮСЬ")
async def rage_start(message: Message):
    kb = [
        [{"text": "ДА ПИЗДЕЦ!", "callback_data": "rage_yes"}],
        [{"text": "Чуть-чуть", "callback_data": "rage_no"}],
        [{"text": "Заебало всё", "callback_data": "rage_fuckall"}],
    ]
    await message.answer("Чё, жопа горит?", reply_markup=InlineKeyboardMarkup(inline_keyboard=kb))

@router.callback_query(F.data.startswith("rage_"))
async def rage_handler(call: CallbackQuery):
    if call.data in RAGE_RESPONSES:
        await call.message.edit_text(
            RAGE_RESPONSES[call.data] + "\n\nДержись, брат. Это пройдёт.",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [{"text": "ЕЩЁ РАЗ!", "callback_data": "rage_yes"}],
                [{"text": "Вроде отпустило", "callback_data": "rage_calm"}]
            ])
        )
    await call.answer()
