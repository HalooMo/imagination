from aiogram.types import InlineKeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton

menuB = [[
    KeyboardButton(text="Назад"),
    KeyboardButton(text="Вперед")
],
[
    KeyboardButton(text="Первое изображение"),
    KeyboardButton(text="Действия")
]
]
operations = [[
    InlineKeyboardButton(text="Сгладить", callback_data="smooth"),
    InlineKeyboardButton(text="Увеличить резкость", callback_data="sharp"),
    InlineKeyboardButton(text="Размыть", callback_data="blur")
],
[
    InlineKeyboardButton(text="Обрезать", callback_data="cut"),
    InlineKeyboardButton(text="Увеличить", callback_data="increas"),
    InlineKeyboardButton(text="Уменьшить ", callback_data="reduce")

],
[
    InlineKeyboardButton(text="Наложить", callback_data="past"),
    InlineKeyboardButton(text="Сжать", callback_data="compress"),
    InlineKeyboardButton(text="Расширить", callback_data="expand")
]]

menu_link = ReplyKeyboardMarkup(keyboard=menuB, resize_keyboard=True)
menu = InlineKeyboardMarkup(inline_keyboard=operations)
