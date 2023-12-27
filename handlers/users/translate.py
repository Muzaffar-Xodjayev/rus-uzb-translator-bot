from aiogram import types, Dispatcher
from googletrans import Translator


translator = Translator()


async def translate_message(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) >= 2:
        if lang == 'uz':
            await message.reply(translator.translate(message.text, dest='ru').text)
        elif lang == 'ru':
            await message.reply(translator.translate(message.text, dest='uz').text)
        else:
            await message.reply(f"Bu Bot bu tildagi gapni tarjima qila olmaydi uzr 🙂")
    else:
        await message.reply("Bunday so'z topilmadi yoki kattaroq gap yozing.\n"
                            "Такое слово не найдено или напишите предложение большего размера 😔")


def register_translate_handler(dp: Dispatcher):
    dp.register_message_handler(translate_message, content_types=["text"])
