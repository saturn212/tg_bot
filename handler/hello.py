from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import router

@router.message(Text("кнопка 1"))
async def hallo(message: types.Message):
    user_input = message.text
    await message.answer(text='вы выбрали кнопку 1')

@router.message(Text("кнопка 2"))
async def hallo(message: types.Message):
    await message.answer(text='вы выбрали кнопку 2')
#
#
# @router.message(Text(contains='привет'))
# async def hello(message: types.Message):
#     await message.answer(text='привет')
#
# @router.message(Text(contains='пока'))
# async def poko(message: types.Message):
#     await message.answer(text='пока')

kb = [

    types.KeyboardButton(text='кнопка 1'),
    types.KeyboardButton(text='кнопка 2'),
]


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for button in kb:
        builder.add(button)
    builder.adjust(2)
    await message.answer(text='вы использовали команду /start'
                         , reply_markup=builder.as_markup(resize_keyboard=True))
