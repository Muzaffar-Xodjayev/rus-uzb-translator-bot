import asyncpg.exceptions
from aiogram import types
from loader import dp, bot, db

from data.config import ADMINS

@dp.chat_join_request_handler()
async def approver(req: types.ChatJoinRequest):
    user_id = req.from_user.id
    chat_id = -1001158456137
    answer_text = "Assalomu alaykum <b>Ruscha va O'zbekcha Tarjimon</b> ga xush kelibsiz!\n"
    answer_text += "Biror gap yozing Ruscha yoki O'zbekchada Tarjimasini qaytaraman.\n"
    answer_text += "Botni ishlash tartibi bilan batafsil /help buyrug'i orqali tanishib chiqing"

    try:
        await bot.approve_chat_join_request(chat_id=chat_id, user_id=user_id)
        await bot.send_message(user_id, answer_text)
    except:
        await bot.send_message(user_id, answer_text)

    name = req.from_user.full_name
    # ADD USER IN DB
    try:
        await db.add_user(
            telegram_id=req.from_user.id,
            full_name=name,
            username=req.from_user.username
        )
        count = await db.select_all_user()
        msg = f"{req.from_user.full_name} bazaga qo'shildi.\nBazada {len(count)} ta foydalanuvchi bor."
        try:
            for user in ADMINS:
                await bot.send_message(user, msg)
        except:
            pass
    except asyncpg.exceptions.UniqueViolationError:
        # pass
        await bot.send_message(req.from_user.id,f"Hurmatli Foydalanuvchi siz Bot ga a'zo bo'lgansiz bemalol foydalanishingiz mumkin.")

