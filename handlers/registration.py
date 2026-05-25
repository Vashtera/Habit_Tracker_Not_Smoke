from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from App.database.requests import add_user

router = Router()

class Register(StatesGroup):
    price = State()
    start_date = State()

@router.callback_query(F.data == "registration")
async def add_new_user(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Register.price)
    await callback.message.answer("Введите стоимость одной пачки сигарет")

@router.message(Register.price)
async def register_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Register.start_date)
    await message.answer("Введите дату, когда ты бросил курить в формате ДД.ММ.ГГГГ")

@router.message(Register.start_date)
async def register_date(message: Message, state: FSMContext):
    data = await state.get_data()
    user_price = float(data.get("price"))
    user_date = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    await add_user(user_id, user_name, user_price, user_date)
    await state.clear()
    await message.answer("Регистрация прошла успешно!")
                                  


