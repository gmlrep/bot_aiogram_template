from aiogram import types, F, Router
from aiogram.enums import ContentType
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from fluent.runtime import FluentLocalization

user_router = Router()


# Обработка команды start
@user_router.message(Command("start"))
async def start_handler(message: Message, l10n: FluentLocalization):
    await message.answer(l10n.format_value('start'))
