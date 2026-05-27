from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from App.database.requests import get_user_by_tg_id

router = Router()

@router.callback_query(F.data == 'change'):
async def 