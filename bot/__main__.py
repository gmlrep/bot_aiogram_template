import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from bot.fluent_loader import get_fluent_localization

from bot.handlers.usermode import user_router
from bot.handlers.adminmode import admin_router
from bot.middlewares.throttling import ThrottlingMiddleware
from bot.config_reader import parse_settings, Settings


async def main():

    config: Settings = parse_settings()
    admin_list = list(map(int, config.bot.admin_list_id.split(',')))

    logging.basicConfig(
        level=logging.INFO,
        # filename='data/logs.log',
        format="%(asctime)s - %(message)s"
    )

    # Loading localization for bot
    l10n = get_fluent_localization(config.bot.language)

    # bot = Bot(token=os.getenv('BOT_TOKEN'))
    bot = Bot(token=config.bot.token.get_secret_value())
    # Create Dispatcher
    dp = Dispatcher(storage=MemoryStorage(), l10n=l10n)

    # Add admin filter to admin_router and user_router
    admin_router.message.filter(F.from_user.id.in_(admin_list))
    user_router.message.filter(~F.from_user.id.in_(admin_list))

    dp.include_router(user_router)
    dp.include_router(admin_router)

    # Registration middleware on throttling
    dp.message.middleware(ThrottlingMiddleware())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
