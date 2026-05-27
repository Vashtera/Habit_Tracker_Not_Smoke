from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from App.database.requests import add_user
from App.keyboards import keyboard_for_excisting_user

router = Router()

class Register(StatesGroup):
    price = State()
    start_date = State()
    cigarettes_in_pack = State()
    cigarettes_per_day = State() 

@router.callback_query(F.data == "registration")
async def add_new_user(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Register.price)
    await callback.message.answer("Введите стоимость одной пачки сигарет")

@router.message(Register.price)
async def register_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await state.set_state(Register.cigarettes_in_pack)
    await message.answer("Введите количество сигарет в Вашей пачке")

@router.message(Register.cigarettes_in_pack)
async def register_pack_size(message: Message, state: FSMContext):
    await state.update_data(cigarettes_in_pack=message.text)
    await state.set_state(Register.cigarettes_per_day)
    await message.answer("Сколько сигарет в день Вы выкуривали?")

@router.message(Register.cigarettes_per_day)
async def register_amount_per_day(message: Message, state: FSMContext):
    await state.update_data(cigarettes_per_day=message.text)
    await state.set_state(Register.start_date)
    await message.answer("Введите дату, когда Вы бросили курить в формате ДД.ММ.ГГГГ")

@router.message(Register.start_date)
async def register_date(message: Message, state: FSMContext):
    data = await state.get_data()
    user_price = float(data.get("price"))
    user_pack = int(data.get("cigarettes_in_pack"))
    user_day = int(data.get("cigarettes_per_day"))
    user_date = message.text
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    await add_user(user_id, user_name, user_price, user_date, user_pack, user_day)
    await state.clear()
    await message.answer("Регистрация прошла успешно!",
                         reply_markup=keyboard_for_excisting_user)
                                  


