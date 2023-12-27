from datetime import datetime
from aiogram import types
from loader import dp, bot
from database.connection import *


@dp.chat_join_request_handler()
async def approver(req: types.ChatJoinRequest):
    user_id = req.from_user.id
    chat_id = req.chat.id
    answer_text = "Assalomu alaykum <b>Ruscha va O'zbekcha Tarjimon</b> ga xush kelibsiz!\n"
    answer_text += "Biror gap yozing Ruscha yoki O'zbekchada Tarjimasini qaytaraman.\n"
    answer_text += "Botni ishlash tartibi bilan batafsil /help buyrug'i orqali tanishib chiqing"

    try:
        await bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
        await bot.send_message(user_id, answer_text)
    except:
        await bot.send_message(user_id, answer_text)

    # ADD USER IN DB
    name = req.from_user.full_name
    user_id = req.from_user.id
    username = req.from_user.username
    join_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    await add_user(user_id, name, username, join_time)
    await bot.send_message(chat_id=user_id, text="🇷🇺 Ruscha va O'zbekcha tarjimon botga xush kelibsiz !!! 🇺🇿\n"
                         "Xabaringizni yozing:")
