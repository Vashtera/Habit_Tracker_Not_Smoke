from datetime import datetime

from aiogram import F, Router
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.enums import ParseMode

from App.database.requests import get_user_by_tg_id

router = Router()

def calculate_profile_data(
        start_date_str: str, 
        price: float,
        cig_in_pack: int,
        cig_per_day: int):
    start_date_obj = datetime.strptime(start_date_str, "%d.%m.%Y").date()
    today = datetime.now().date()
    days_without_smoke = (today - start_date_obj).days

    one_cig_price = price / cig_in_pack
    total_cigarettes_not_smoked = days_without_smoke * cig_per_day

    total_save = total_cigarettes_not_smoked * one_cig_price
    return days_without_smoke, total_cigarettes_not_smoked, round(total_save, 2)

@router.callback_query(F.data == 'profile')
async def show_profile(callback: CallbackQuery):
    await callback.answer()
    user = await get_user_by_tg_id(callback.from_user.id)
    cig_in_pack = user[6]
    cig_per_day = user[7]
    user_price = user[3]
    user_date = user[4]
    days, cigs, money = calculate_profile_data(user_date, user_price, cig_in_pack, cig_per_day)
    await callback.message.answer(
        f"Привет! <b>{callback.from_user.full_name}</b>\n\n"
        f"Ваше имя - {callback.from_user.username or "Empty"}\n"
        f"Дата начала - {user_date}\n"
        f"Дней без курения - {days}\n"
        f"Не выкурено сигарет - {cigs}\n"
        f"Сэкономлено денег - {money}",
        parse_mode=ParseMode.HTML,
        reply_markup=ReplyKeyboardRemove()
    )
    

