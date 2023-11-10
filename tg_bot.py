import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Text, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

TOKEN = '6411481932:AAGLTUNo75tEWf3_InbIehpP9ute9dnXUEo'

router = Router()

@router.message(Text(contains='привет'))
async def hello(message: types.Message):
    await message.answer(text='привет')

@router.message(Text(contains='пока'))
async def poko(message: types.Message):
    await message.answer(text='пока')

kb = [

    types.KeyboardButton(text='кнопка 1'),
    types.KeyboardButton(text='кнопка 1'),
]

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for button in kb:
        builder.add(button)
    builder.adjust(2)
    await message.answer(text='вы использовали команду /start'
                              , reply_markup= builder.as_markup(resize_keyboard=True))

@router.message(Text("кнопка 1"))
async def hallo(message: types.Message):
    await message.answer(text='вы выбрали кнопку 1')


async def main():
    dp = Dispatcher()
    dp.include_router(router)
    bot = Bot(TOKEN, parse_mode="HTML")
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
