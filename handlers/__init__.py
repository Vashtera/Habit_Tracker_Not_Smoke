from aiogram import Dispatcher

from .start import router as start_router
from .registration import router as reg_router


def register_routers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(reg_router)