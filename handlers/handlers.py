from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

# Command handler
@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет {message.from_user.full_name}\n я трекер твоего отказа от курения")


