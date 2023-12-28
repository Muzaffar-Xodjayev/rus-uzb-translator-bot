from datetime import datetime
from aiogram import types, Dispatcher

from database.connection import *
from utils.misc.check_subs import check_sub_channels
from keyboards.inline.channels import show_channel_btn


async def bot_start(message: types.Message):
    name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    join_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    text = f"🇷🇺 Ruscha va O'zbekcha tarjimon botga xush kelibsiz !!! 🇺🇿\n" \
           f"Xabaringizni yozing:"
    await add_user(user_id, name, username, join_time)
    channels = await get_all_channels()
    if channels:
        is_follow = await check_sub_channels(user_id, channels)
        if is_follow:
            await message.answer(text)
        else:
            btn = await show_channel_btn(channels)
            await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling.", reply_markup=btn)
    else:
        await message.answer(text)


async def check_followed_user(call: types.CallbackQuery):
    user_id = call.from_user.id
    channels = await get_all_channels()
    is_follow = await check_sub_channels(user_id, channels)
    text = f"🇷🇺 Ruscha va O'zbekcha tarjimon botga xush kelibsiz !!! 🇺🇿\n" \
           f"Xabaringizni yozing:"
    if is_follow:
        await call.message.delete()
        await call.message.answer(text)
    else:
        await call.answer("Berilgan kanallarga obuna bo'ling 👇", show_alert=True)


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=["start"])
    dp.register_callback_query_handler(check_followed_user, text="channel:followed")
