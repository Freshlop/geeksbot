from aiogram import types, Dispatcher
from random import choice
from config import bot
async def delete_sticker(message: types.Message):
    await message.delete()


# @dp.message_handler()
async def bad_words_filter(message: types.Message):
    bad_words = ['html', 'js', 'css', 'жинди', 'дурак']
    for word in bad_words:
        if word in message.text.lower().replace(' ', ''):
            await message.answer(f"Не матерись {message.from_user.full_name}, "
                                 f"сам ты {word}")
            await message.delete()
            # await bot.delete_message(message.chat.id, message.message_id)
            break

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text == "game":
        list1 = [ '⚽️', '🏀', '🎲', '🎰', '🎯', '🎳']
        emoji = choice(list1)
        await bot.send_message(message.chat.id,text=emoji)



def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_words_filter, content_types=['text'])
    dp.register_message_handler(delete_sticker, content_types=['sticker', 'photo',
                                                               'animation'])