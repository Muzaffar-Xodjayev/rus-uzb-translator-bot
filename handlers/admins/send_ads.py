import asyncio

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked

from database.connection import *
from states.ads import Message
from .intro import intro_admin
from handlers.users.start import bot_start
from handlers.users.help import help_user
from keyboards.inline.admin_command import cancel_btn
from loader import bot


async def intro_ads(call: types.CallbackQuery):
    await call.answer()
    btn = await cancel_btn()
    await call.message.edit_text("Xabaringizni Yuboring: ", reply_markup=btn)
    await Message.text.set()


async def send_msg(msg: types.Message, state: FSMContext):
    if msg.text == "/start":
        await msg.answer("Bekor Qilindi ❌")
        await state.finish()
        await bot_start(msg)
    elif msg.text == "/help":
        await msg.answer("Bekor Qilindi ❌")
        await state.finish()
        await help_user(msg)
    else:
        users = await get_all_users()
        text_caption = msg.caption
        text_type = msg.content_type
        text = msg.html_text
        rep_btn = msg.reply_markup

        send_user = 0
        send_error = 0
        for user in users:
            user_id = user["telegram_id"]
            try:
                if text_type == 'sticker':
                    return
                elif text_type == 'text':
                    await bot.send_message(chat_id=user_id, text=text, reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'video':
                    await bot.send_video(user_id, msg.video.file_id, caption=text_caption, reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'photo':
                    await bot.send_photo(user_id, msg.photo[-1].file_id, caption=text_caption, reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'audio':
                    await bot.send_audio(user_id, msg.audio, reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                elif text_type == 'location':
                    lat = msg.location['latitude']
                    lon = msg.location['longitude']
                    await bot.send_location(chat_id=user_id, latitude=lat, longitude=lon, reply_markup=rep_btn)
                    await asyncio.sleep(0.05)
                send_user += 1
            except Exception:
                send_error += 1
                continue
        if send_user == 0:
            await bot.send_message(msg.from_user.id, 'Xech kimga yuborilmadi')
        else:
            await bot.send_message(msg.from_user.id,
                                   f"Jonatildi: <b>{send_user + send_error}</b> ta foydalanuvchiga\n"
                                   f"Aktiv A'zolar: <b>{send_user}</b> ta \n"
                                   f"Ban bergan a'zolar: <b>{send_error}</b> ta\n")
        await state.finish()


async def cancel_func(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("Bekor qilindi")
    await intro_admin(call.message)


def register_send_ads_handler(dp: Dispatcher):
    dp.register_callback_query_handler(intro_ads, text="admin:send_msg")
    dp.register_callback_query_handler(cancel_func, state=Message.text, text="admin:cancel")
    dp.register_message_handler(send_msg, state=Message.text,
                                content_types=['text', 'video', 'photo', 'audio', 'location'])
