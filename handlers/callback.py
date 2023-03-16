from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


# @dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_2")
    markup.add(button_1)

    question = "Сколько яблок на березе??"
    answer = [
        "12",
        "3",
        "БЕССКОНЕЧНОСТЬ",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_3")
    markup.add(button_1)
    question = "Сколько??"
    answer = [
        '4',
        '8',
        '4, 6',
        '2, 4',
        '5',
    ]

    photo = open("media/problem1.jpg", "rb")
    await bot.send_photo(call.from_user.id, photo=photo)

    await bot.send_poll(
        reply_markup=markup,
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Стыдно не знать",
        # open_period=5,
    )


async def quiz_4(call: types.CallbackQuery):


    question = "сколько 2 + 2"
    answer = [
        "12",
        "4",
        "БЕССКОНЕЧНОСТЬ",
        "0",
        "-10",
        "999",
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=5,

    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_1")
    dp.register_callback_query_handler(quiz_3, text="button_2")
    dp.register_callback_query_handler(quiz_4, text="button_3")