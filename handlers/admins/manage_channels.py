from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from handlers.admins.intro import intro_admin
from handlers.users.help import help_user
from handlers.users.start import bot_start
from states.ads import Channel
from filters.is_admin import IsAdmin
from keyboards.inline.channels import manage_channels, channels_list_btn
from keyboards.inline.admin_command import cancel_btn
from database.connection import *


async def show_channels(call: types.CallbackQuery):
    await call.answer()
    channels = await get_all_channels()
    btn = await manage_channels(channels)
    await call.message.edit_text("Kanallar: ", reply_markup=btn)


async def manage_channel(call: types.CallbackQuery):
    await call.answer()
    data = call.data.split(":")[1]
    if data == "plus":
        btn = await cancel_btn()
        await call.message.edit_text("Menga yuboring: Kanal ID + Kanal Nomi + Kanal Link", reply_markup=btn)
        await Channel.body.set()
    elif data == "minus":
        channel = await get_all_channels()
        btn = await channels_list_btn(channel)
        await call.message.edit_text("Qaysi kanalni o'chirmoqchisiz", reply_markup=btn)
    else:
        await call.message.delete()
        await intro_admin(call.message)


async def remove_channel(call: types.CallbackQuery):
    await call.answer()
    channel_id = call.data.split(":")[1]
    if channel_id == "cancel":
        await call.message.delete()
        await call.message.answer("Bekor Qilindi ❌")
        await intro_admin(call.message)
    else:
        await delete_channel(channel_id)
        await call.message.edit_text("✅ Kanal muvaffaqiyatli o'chirildi")
        await intro_admin(call.message)


async def add_channel(message: types.Message, state: FSMContext):
    # text = message.text
    _ = message.text.replace(" + ", "+")
    if _ == "/start":
        await message.answer("Bekor Qilindi ❌")
        await state.finish()
        await bot_start(message)
    elif _ == "/help":
        await message.answer("Bekor Qilindi ❌")
        await state.finish()
        await help_user(message)
    else:
        text = _.split("+")
        if len(text) == 3:
            await save_channel(text[0], text[1], text[2])
            await message.answer("✅ Kanal muvaffaqiyatli qo'shildi.")
            await intro_admin(message)
            await state.finish()
        else:
            await message.answer("❗️ Kanal talablari to'liq emas.")


async def cancel_func(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("Bekor qilindi")
    await intro_admin(call.message)


def register_manage_channels_handler(dp: Dispatcher):
    dp.register_callback_query_handler(show_channels, IsAdmin(), text=["admin:channels"])
    dp.register_callback_query_handler(manage_channel, IsAdmin(), text_contains="manage_channel:")
    dp.register_callback_query_handler(cancel_func, state=Channel.body, text="admin:cancel")
    dp.register_message_handler(add_channel, state=Channel.body, content_types=["text"])
    dp.register_callback_query_handler(remove_channel, text_contains="delete_channel:")
