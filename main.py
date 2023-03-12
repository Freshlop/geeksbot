from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from decouple import config
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = config("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Hello world!")


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer("Сам разбирайся!")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_1 = InlineKeyboardButton("NEXT", callback_data="button_1")
    markup.add(button_1)

    question = "Кем был Чингыз Айтматов?"
    answer = [
        "Поэт",
        "писатель",
        "драматург",

    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_1")
async def quiz_2(call: types.CallbackQuery):
    question = "Кто написал Гарри Поттера?"
    answer = [
        "Джоан Роулинг ",
        "Чынгыз Айтматов",
        "Леонардо Да Винчи",
        "А.Пушкин",

    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=7,
    )

@dp.message_handler(commands=["mem"])
async def mem (message: types.Message):
    photo = open("media/meme.jpg", 'rb')
    await bot.send_photo(message.from_user.id, photo = photo)


@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isdigit():
        await message.answer(f"{int(message.text)**2}")
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text=message.text
        )
        await message.answer(f"This is an answer method! {message.message_id}")
        await message.reply("This is a reply method!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)










