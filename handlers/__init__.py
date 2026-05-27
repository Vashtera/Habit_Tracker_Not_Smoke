from aiogram import Dispatcher

from .start import router as start_router
from .registration import router as reg_router
from .profile import router as profile_router
from .changes import router as change_router


def register_routers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(reg_router)
    dp.include_router(profile_router)
    dp.include_router(change_router)