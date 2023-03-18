from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import client_kb
from uuid import uuid4
from config import ADMINS


class FSMAdmin(StatesGroup):
    id1 = State()
    name = State()
    age = State()
    direction = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == "private" and message.chat.id in ADMINS:
        await FSMAdmin.name.set()
        await message.answer("Ваше id готово!", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши в группу!")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] =str(uuid4())
    await FSMAdmin.next()
    await message.answer("Как вас зовут?",  reply_markup=client_kb.cancel_markup)

async def load_name(message:types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Сколько вам лет?',  reply_markup=client_kb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числами!")
    elif int(message.text) < 16 or int(message.text) > 40:
        await message.answer("Возростное ограничение",  reply_markup=client_kb.cancel_markup)
    else:
        async with state.proxy() as data:
            data['age'] = message.text
        await FSMAdmin.next()
        await message.answer("Какое у вас направление?",  reply_markup=client_kb.cancel_markup)


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("Ваща группа?", reply_markup=client_kb.cancel_markup)


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMAdmin.next()
    await message.answer("отлично?", reply_markup=client_kb.submit_markup)


# async def load_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = message.photo[0].file_id
#         await message.answer_photo(
#             photo=data['photo'],
#             caption=f"{data['name']} {data['age']} {data['gender']} {data['region']}\n"
#                     f"@{data['username']}"
#         )
#     await FSMAdmin.next()
#     await message.answer("Все верно?", reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state: FSMContext):
    if message.text == "ДА":
        # Подключение БД
        await state.finish()
        await message.answer("Ты зареган!")
    elif message.text == "НЕТ":
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer("Нормально пиши!")


async def cancel_reg(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state:
        await state.finish()
        await message.answer("Отменено")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_reg,
                                Text(equals="cancel", ignore_case=True), state='*')

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    # dp.register_message_handler(load_photo, state=FSMAdmin.photo,
    #                             content_types=['photo'])
    dp.register_message_handler(submit, state=FSMAdmin.submit)