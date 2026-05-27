from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from App.database.requests import get_user_by_tg_id

router = Router()

class Change(StatesGroup):
    new_price = State()

@router.callback_query(F.data == 'change')
async def add_new_price(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(Change.new_price)
    await callback.message.answer("Введите новую стоимость пачки сигарет")

@router.message(Change.new_price)
async def change_with_new_price(message: Message, state: FSMContext):
    new_price = float(message.text)
    user = await get_user_by_tg_id(message.from_user.id)
    user_old_date = user[4]
    user_old_price = user[3]
    user_cig_in_pack = user[6]
    user_cig_per_day = user[7]
    user_saved_money = user[5]