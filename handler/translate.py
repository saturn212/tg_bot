from aiogram import types
from aiogram.filters import Command, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import router,user_list
from keys.key import kb_translation



@router.message(Command("choice"))
async def hallo(message: types.Message):
    builder = InlineKeyboardBuilder()
    for button in kb_translation:
        builder.add(button)
    builder.adjust(2)
    await message.answer(text=f'выберите язык',
                         reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(startswith='lan'))
async def choice(callback:types.CallbackQuery):
    lan = callback.data[-2:]
    id_user = callback.message.chat.id
    user_list[id_user] = lan

