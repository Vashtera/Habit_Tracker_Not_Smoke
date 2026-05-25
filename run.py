import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers.start import router
from App.database.db import create_tables

dp = Dispatcher()

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    dp.include_router(router)
    await create_tables()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")