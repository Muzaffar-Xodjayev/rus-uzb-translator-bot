from handlers.users.start import register_start_handler
from handlers.users.help import register_help_handler
from handlers.users.translate import register_translate_handler
from handlers.admins.intro import register_intro_admin_handler
from handlers.admins.send_ads import register_send_ads_handler


async def launch_handlers(dispatcher):
    register_intro_admin_handler(dispatcher)
    register_start_handler(dispatcher)
    register_help_handler(dispatcher)
    register_translate_handler(dispatcher)
    register_send_ads_handler(dispatcher)
