from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.dispatcher.flags import get_flag
from aiogram.types import Message
from cachetools import TTLCache

from bot.config_reader import parse_settings, Settings

config: Settings = parse_settings()


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, time_limit: int = config.bot.throttling):
        self.limit = TTLCache(maxsize=10000, ttl=time_limit)

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any],
    ) -> Any:
        if event.chat.id in self.limit:
            print("To many requests!")
            return
        else:
            self.limit[event.chat.id] = None
        return await handler(event, data)
