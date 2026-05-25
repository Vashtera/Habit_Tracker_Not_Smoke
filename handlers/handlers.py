from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
import App.keyboards as kb

router = Router()

# This command shows the keyboard only for existing users(NEED TO CHANGE)
@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет {message.from_user.full_name}\n я трекер твоего отказа от курения",
                         reply_markup=kb.keyboard_for_excisting_user)

# This async func shows a profile of user
@router.callback_query(F.data == "profile")
async def show_profile(callback: CallbackQuery):
    await callback.answer("Вы выбрали профиль")
    await callback.message.answer(f"Привет {callback.from_user.full_name}!")
    





