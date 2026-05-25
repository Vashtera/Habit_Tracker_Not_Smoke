from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
import App.keyboards as kb

router = Router()

# Command handler
@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет {message.from_user.full_name}\n я трекер твоего отказа от курения",
                         reply_markup=await kb.inline_cars())

@router.message(Command("hi"))
async def say_hi(message: Message):
    await message.answer("Hi!")

@router.message(F.text == "Hi")
async def say_hello(message: Message):
    await message.answer("Hello")