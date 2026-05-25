from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

import App.keyboards as kb
from App.database.requests import get_user_by_tg_id

router = Router()

class Register(StatesGroup):
    price = State()
    start_date = State()

@router.callback_query(F.data == "registration")
async def add_new_user(callback: CallbackQuery, state: FSMContext):
    await callback.answer()


