from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache

from bot.db.config import settings


class ThrottlingMiddleware(BaseMiddleware):

    def __init__(self, time_limit: int = settings.bot.throttling):
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
