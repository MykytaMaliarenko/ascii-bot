import re

from telegram import Message, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

from .decode_binary import ACTION_DECODE_BINARY
from .decode_hex import ACTION_DECODE_HEX
from .encode_ascii import ACTION_ENCODE_ASCII


ENGLISH_TEXT_REGEX = r'^[!@#$%^&*(),.?":{};|<>№A-z0-9\s]+$'
BINARY_REGEX = r'^[0-1\s]+$'
HEX_REGEX = r'[0-9A-Ea-e\s]+$'


def on_text_input(update: Update, context: CallbackContext):
    message: Message = update.message

    keyboard = []
    if bool(re.fullmatch(ENGLISH_TEXT_REGEX, message.text)):
        keyboard.append([InlineKeyboardButton("Перевести в ASCII", callback_data=ACTION_ENCODE_ASCII)])

    if bool(re.fullmatch(BINARY_REGEX, message.text)):
        keyboard.append(([InlineKeyboardButton("Перевести из 2-ичной системы", callback_data=ACTION_DECODE_BINARY)]))

    if bool(re.fullmatch(HEX_REGEX, message.text)):
        keyboard.append([InlineKeyboardButton("Перевести из 16-ичной системы", callback_data=ACTION_DECODE_HEX)])

    if len(keyboard) != 0:
        message.reply_text("Доступные действия:", reply_markup=InlineKeyboardMarkup(keyboard), quote=True)
    else:
        message.reply_text("Нету доступных действий(текст должен быть написан латинскими буквами)", quote=True)
