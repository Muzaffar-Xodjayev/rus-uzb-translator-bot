from aiogram import executor
from loader import dp
from utils.set_bot_commands import set_default_commands
from launcher_handler import launch_handlers


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await launch_handlers(dispatcher)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
