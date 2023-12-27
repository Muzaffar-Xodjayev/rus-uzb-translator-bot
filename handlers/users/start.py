from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.builtin import CommandStart


async def bot_start(message: types.Message):
    name = message.from_user.full_name
    await message.answer("hello")
    print("sent start")


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, CommandStart())
