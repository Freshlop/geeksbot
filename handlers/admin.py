

from aiogram import types, Dispatcher
from config import ADMINS, bot


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("ТЫ НЕ МОЙ БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(f"{message.from_user.first_name} братан кикнул "
                                 f"{message.reply_to_message.from_user.full_name}")
    else:
        await message.answer("Пиши в группе!")

async def pin(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINS:
            await message.answer("ТЫ НЕ МОЙ БОСС!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await bot.pin_chat_message(message.chat.id,message.reply_to_message.message_id)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(pin,commands=["pin"], commands_prefix='!/')

