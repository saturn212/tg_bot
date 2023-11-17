from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from loader import router

class Reg_form(StatesGroup):
    name = State()
    age = State()


@router.message(Command("reg"))
async def start_reg(message: types.Message, state, FSMContext):
    await state.set_state(Reg_form.name)
    await message.answer('введите своё имя')

@router.message(Reg_form.name)
async def get_name(message: types.Message, state, FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg_form.age)
    await message.answer('введите свой возраст')

@router.message(Reg_form.age)
async def get_age(message: types.Message, state, FSMContext):
    await state.update_data(name=message.text)




