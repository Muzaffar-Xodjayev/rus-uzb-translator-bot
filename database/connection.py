from playhouse.shortcuts import model_to_dict
from database.models import *
from data.config import ADMINS
from loader import bot, db


async def add_user(user_id, name, username, join_time):
    with db:
        if not Users.select().where(Users.telegram_id == user_id).exists():
            Users.create(
                telegram_id=user_id,
                full_name=name,
                username=username,
                join_date=join_time,
            )
            count = Users.select()

            msg = f"<a href='tg://user?id={6202185692}'>{name}</a> Bazaga qo'shildi. " \
                  f"\nBazada {len(count)} foydalanuvchi bor"
            for user in ADMINS:
                await bot.send_message(user, msg)


async def get_all_users():
    with db:
        usr = Users.select()
        user = [model_to_dict(item) for item in usr]
        return user


async def get_one_by_id(telegram_id):
    with db:
        usr = Users.select().where(Users.telegram_id == telegram_id)
        user = [model_to_dict(item) for item in usr]
        return user
