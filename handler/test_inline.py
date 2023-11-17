from aiogram import types
from aiogram.filters import Command, Text
from aiogram.utils.keyboard import InlineKeyboardBuilder
from loader import router
from keys.key import kb_translation
from random import randint

@router.message(Command("random"))
async def get_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    for button in kb_translation:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text=f'выберите язык',
                         reply_markup=builder.as_markup(resize_keyboard=True))

@router.callback_query(Text('rundom_num'))
async def choice(callback:types.CallbackQuery):
    num = randint(1, 10)
    await callback.message.answer(f'Твоё число:{num}')


