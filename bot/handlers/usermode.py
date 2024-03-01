from aiogram import types, F, Router
from aiogram.enums import ContentType
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from fluent.runtime import FluentLocalization

from bot.db.requests import insert_user

user_router = Router()


# Обработка команды start
@user_router.message(Command("start"))
async def start_handler(message: Message, l10n: FluentLocalization):
    await insert_user(user_id=message.from_user.id,
                      username=message.from_user.username,
                      fullname=message.from_user.full_name)
    await message.answer(l10n.format_value('start'))
    print(type(message.from_user.id))
