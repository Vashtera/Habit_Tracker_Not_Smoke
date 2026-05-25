from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

import App.keyboards as kb
from App.database.requests import get_user_by_tg_id

router = Router()

# This command shows the keyboard only for existing users(NEED TO CHANGE)
@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    user = await get_user_by_tg_id(message.from_user.id)
    if user is None:
        await message.answer("Привет новый пользователь, для продолжения работы нужно зарегистрироваться",
                             reply_markup=kb.keyboard_for_unexcisting_user)
    else:
        await message.answer(f"Привет {message.from_user.full_name}\nЯ трекер твоего отказа от курения",
                         reply_markup=kb.keyboard_for_excisting_user)

    





