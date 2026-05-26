from datetime import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.enums import ParseMode

from App.database.requests import get_user_by_tg_id

router = Router()

def calculate_profile_data(start_date_str: str, price: float):
    start_date_obj = datetime.strptime(start_date_str, "%d.%m.%Y").date()
    today = datetime.now().date()
    days_without_smoke = (today - start_date_obj).days

    total_save = days_without_smoke * price
    return days_without_smoke, total_save

@router.callback_query(F.data == 'profile')
async def show_profile(callback: CallbackQuery):
    await callback.answer()
    user = await get_user_by_tg_id(callback.from_user.id)
    user_price = user[3]
    user_date = user[4]
    days, money = calculate_profile_data(user_date, user_price)
    await callback.message.answer(
        f"<b>{callback.from_user.full_name}</b>\n\n"
        f"Username - {callback.from_user.username or "Empty"}\n"
        f"Starting date - {user_date}\n"
        f"Days without smoke - {days}\n"
        f"Money saved - {money}",
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove()
    )
    

