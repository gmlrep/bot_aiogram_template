from aiogram.utils.keyboard import InlineKeyboardBuilder
from fluent.runtime import FluentLocalization


# Пример клавиатуры
def kb_menu(l10n: FluentLocalization):
    menu = InlineKeyboardBuilder()
    menu.button(text="button", callback_data='btn1')
    menu.adjust(1, 1)
    return menu.as_markup()
