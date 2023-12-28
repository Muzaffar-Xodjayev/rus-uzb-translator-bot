from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_channel_btn(channels):
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(*[InlineKeyboardButton(text=f"📌 ️{item['channel_name']}",
                                        url=f"{item['channel_url']}") for item in channels],)
    btn_done = InlineKeyboardButton(text="✅ Obuna Bo'ldim", callback_data="channel:followed")
    keyboard.add(btn_done)
    return keyboard


async def manage_channels(channels):
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(*[InlineKeyboardButton(text=f"{item['channel_name']}",
                                        url=f"{item['channel_url']}") for item in channels], )
    plus = InlineKeyboardButton(text="➕ Qo'shish", callback_data="manage_channel:plus")
    minus = InlineKeyboardButton(text="➖ O'chirish", callback_data="manage_channel:minus")
    keyboard.row(plus, minus)
    return keyboard


async def channels_list_btn(channels):
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        *[InlineKeyboardButton(f"{item['channel_name']} - ❌", callback_data=f"delete_channel:{item['channel_id']}")
          for item in channels]
    )
    cancel = InlineKeyboardButton(text="❌ Bekor qilish", callback_data="delete_channel:cancel")
    btn.add(cancel)
    return btn
