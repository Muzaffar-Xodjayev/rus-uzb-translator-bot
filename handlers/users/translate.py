from aiogram import types, Dispatcher
from googletrans import Translator

from database.connection import *
from utils.misc.translator import translator
from utils.misc.check_subs import check_sub_channels
from keyboards.inline.channels import show_channel_btn


async def translate_message(message: types.Message):
    user_id = message.from_user.id
    channels = await get_all_channels()
    if channels:
        is_follow = await check_sub_channels(user_id, channels)
        if is_follow:
            await translator(message)
        else:
            btn = await show_channel_btn(channels)
            await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling.", reply_markup=btn)

    # IF THERE NO CHANNEL IN DB BOT DON'T ASK TO FOLLOW
    else:
        await translator(message)


def register_translate_handler(dp: Dispatcher):
    dp.register_message_handler(translate_message, content_types=["text"])
