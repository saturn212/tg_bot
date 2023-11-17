
from aiogram import Bot, Dispatcher, Router
TOKEN = '6411481932:AAGLTUNo75tEWf3_InbIehpP9ute9dnXUEo'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN, parse_mode="HTML")
user_list ={}

