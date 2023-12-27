from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def admin_command():
    keyboard = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text="📨 Xabar yuborish", callback_data="admin:send_msg")
    btn2 = InlineKeyboardButton(text="📣 Kanallar", callback_data="admin:channels")
    keyboard.add(btn1, btn2)
    return keyboard


async def cancel_btn():
    keyboard = InlineKeyboardMarkup(row_width=1)
    btn = InlineKeyboardButton("❌ Bekor qilish", callback_data="admin:cancel")
    keyboard.add(btn)
    return keyboard
