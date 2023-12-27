from handlers.users.start import register_start_handler
from handlers.users.help import register_help_handler
from handlers.users.translate import register_translate_handler


async def launch_handlers(dispatcher):
    register_start_handler(dispatcher)
    register_help_handler(dispatcher)
    register_translate_handler(dispatcher)
