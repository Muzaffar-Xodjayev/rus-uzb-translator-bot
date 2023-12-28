from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_channel_btn(channels):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*[InlineKeyboardButton(text=f"📌 ️{item['channel_name']}",
                                        url=f"{item['channel_url']}") for item in channels],)
    btn_done = InlineKeyboardButton(text="✅ Obuna Bo'ldim", callback_data="channel:followed")
    keyboard.add(btn_done)
    return keyboard
