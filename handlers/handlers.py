from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message

router = Router()

# Command handler
@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет {message.from_user.full_name}\n я трекер твоего отказа от курения")

@router.callback_query(F.data == "profile")
async def show_profile(callback: CallbackQuery):
    await callback.answer("Вы выбрали профиль")
    await callback.message.answer(f"Hi {callback.from_user.full_name}")


