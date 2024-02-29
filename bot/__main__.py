import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from bot.fluent_loader import get_fluent_localization

from bot.handlers.usermode import user_router
from bot.handlers.adminmode import admin_router


# Loading localization for bot
l10n = get_fluent_localization('ru')

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(storage=MemoryStorage(), l10n=l10n)

# Transform str in int
admin_list = list(map(int, os.getenv('ADMIN_LIST_ID').split(',')))


async def main():

    logging.basicConfig(
        level=logging.INFO,
        # filename='data/logs.log',
        format="%(asctime)s - %(message)s"
    )

    # Add admin filter to admin_router and user_router
    admin_router.message.filter(F.from_user.id.in_(admin_list))
    user_router.message.filter(~F.from_user.id.in_(admin_list))

    dp.include_router(user_router)
    dp.include_router(admin_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
