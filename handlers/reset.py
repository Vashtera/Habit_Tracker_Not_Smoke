from datetime import datetime

from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

from App.database.requests import get_user_by_tg_id, reset_user_progress

router = Router()

@router.callback_query(F.data == 'restart')
async def reset_all_button(callback: CallbackQuery):
    await callback.answer()
    today_obj = datetime.now().date().strftime("%d.%m.%Y")
    await reset_user_progress(callback.from_user.id, today_obj)
    await callback.message.answer("Прогресс сброшен, не отчаивайтесь и пробуйте дальше")