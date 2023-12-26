from data.config import CHANNELS
from loader import bot


async def check_sub_channels(message):
    for channel in CHANNELS:
        check = await bot.get_chat_member(chat_id='-100' + str(channel[1]), user_id=message.from_user.id)
        if check.status == 'left':
            return False

    return True