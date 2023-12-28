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

            msg = f"<a href='tg://user?id={user_id}'>{name}</a> Bazaga qo'shildi. " \
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


async def save_channel(channel_id, channel_name, channel_url):
    with db:
        if not Channels.select().where(Channels.channel_id == channel_id).exists():
            Channels.create(channel_id=channel_id, channel_name=channel_name, channel_url=channel_url)


async def get_all_channels():
    with db:
        return [model_to_dict(item) for item in Channels.select()]


async def delete_channel(channel_id):
    with db:
        Channels.delete().where(Channels.channel_id == channel_id).execute()
