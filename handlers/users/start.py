from datetime import datetime
from aiogram import types, Dispatcher
from database.connection import *


async def bot_start(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    join_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    await add_user(user_id, name, username, join_time)
    await message.answer("🇷🇺 Ruscha va O'zbekcha tarjimon botga xush kelibsiz !!! 🇺🇿\n"
                         "Xabaringizni yozing:")


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["start"])
