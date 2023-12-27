from aiogram import types, Dispatcher
from filters.is_admin import IsAdmin
from keyboards.inline.admin_command import admin_command
from database.connection import *


async def intro_admin(message: types.Message):
    btn = await admin_command()
    users = await get_all_users()
    text = f"Xush Kelibsiz – ADMIN\n" \
           f"Bazada {len(users)} ta foydalanuvchi bor."
    await message.answer(text, reply_markup=btn)


def register_intro_admin_handler(dp: Dispatcher):
    dp.register_message_handler(intro_admin, IsAdmin(), commands=["admin"])
