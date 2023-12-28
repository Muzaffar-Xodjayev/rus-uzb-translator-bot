from aiogram import types, Dispatcher
from filters.is_admin import IsAdmin
from keyboards.inline.admin_command import admin_command
from database.connection import *


async def channels(call: types.CallbackQuery):
    await call.answer()


def register_manage_channels_handler(dp: Dispatcher):
    dp.register_callback_query_handler(channels, IsAdmin(), text=["admin:channels"])
