import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import register_routers 
from App.database.db import create_tables

dp = Dispatcher()

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    register_routers(dp)
    await create_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")