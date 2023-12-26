from aiogram import types
from googletrans import Translator
from utils.misc.subs import check_sub_channels
from keyboards.inline.subs import show_channels
from loader import dp, bot


translator = Translator()


@dp.message_handler()
async def send_message(message: types.Message):
    is_subs = await check_sub_channels(message)
    if is_subs:
        lang = translator.detect(message.text).lang
        if len(message.text.split())>=2:
            try:
                if lang == 'uz':
                    await message.reply(translator.translate(message.text, dest='ru').text)
                elif lang == 'ru':
                    await message.reply(translator.translate(message.text, dest='uz').text)
                else:
                    await message.reply(f"Bu Bot bu tildagi gapni tarjima qila olmaydi uzr 🙂")
            except:
                await message.answer(f"Ma'noliroq gap yozing iltimos.\nПожалуйста, напишите более осмысленное предложение 🙏")
        else:
            await message.reply("Bunday so'z topilmadi yoki kattaroq gap yozing.\nТакое слово не найдено или напишите предложение большего размера 😔")
    else:
        btn = await show_channels()
        context = f"Xurmatli {message.from_user.full_name} botni ishlatishdan oldin quyidagi kanallarga obuna bo'ling 👇"
        await message.answer(text=context, reply_markup=btn)