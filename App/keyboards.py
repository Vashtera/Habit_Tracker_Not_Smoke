from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard_for_excisting_user = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Профиль", callback_data="profile"),
     InlineKeyboardButton(text="Мой прогресс", callback_data="my_progress")], 
    [InlineKeyboardButton(text="Изменить данные", callback_data="change"),
    InlineKeyboardButton(text="Я сорвался", callback_data="restart")]
],
    resize_keyboard=True,
    input_field_placeholder="Выберите опцию")

keyboard_for_unexcisting_user = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Зарегистроваться", callback_data="registration")]
],
    resize_keyboard=True)
