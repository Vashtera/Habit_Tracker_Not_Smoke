from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

import App.keyboards as kb
from App.database.requests import get_user_by_tg_id

router = Router()

@router.callback_query(F.data == "registration")
async def add_new_user():


