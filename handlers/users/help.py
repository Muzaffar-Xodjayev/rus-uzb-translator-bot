from aiogram import types, Dispatcher


async def help_user(message: types.Message):
    msg = f"Bot Tomonidan foydalanuvchiga yordam ko'rsatish bo'limi\n" \
          f"Buyruqlar:\n/start — Botni ishga tushirish\n" \
          f"/help — Yordam Ko'rsatish va Bot ishlash tartibi\n\n" \
          f"<b>Botni ishlash tartibi</b>\n\n" \
          f"1.Agar Siz yozgan matn biror manoga ega bo'lsa va mazmuni bo'lsa bu bot sizga yozgan matningizni " \
          f"Rus yoki O'zbek tilida tarjimasini qaytaradi.\n" \


    await message.reply(msg)


def register_help_handler(dp: Dispatcher):
    dp.register_message_handler(help_user, commands="help")
