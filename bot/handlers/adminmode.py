from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

admin_router = Router()


# Обработка команды start
@admin_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer('Привет, админ!')
