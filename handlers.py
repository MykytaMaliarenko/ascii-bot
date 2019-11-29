import re
from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

GREETING = "Hi!\nI can encode text in ascii by pairing or unpairing " \
           "and convert it to hex system.\nJust write text and you " \
           "will see all available actions.\nGL =)"


def start(update: Update, context: CallbackContext):
    message: Message = update.message
    message.reply_text(GREETING)


encode_ascii_action, decode_binary, decode_hex = range(3)

ASCII_REGEX = r"^[?!\().\dA-z]+$"
BINARY_REGEX = r"^[0-1]+$"
HEX_REGEX = r"^[0-9A-e]+$"


def on_text_input(update: Update, context: CallbackContext):
    message: Message = update.message

    keyboard = []
    if bool(re.fullmatch(ASCII_REGEX, message.text)):
        keyboard.append([InlineKeyboardButton("encode in ascii", callback_data=encode_ascii_action)])

    if bool(re.fullmatch(BINARY_REGEX, message.text)):
        keyboard.append(([InlineKeyboardButton("decode from binary", callback_data=decode_binary)]))

    if bool(re.fullmatch(HEX_REGEX, message.text)):
        keyboard.append([InlineKeyboardButton("decode from hex", callback_data=decode_hex)])

    message.reply_text("Available Actions:", reply_markup=InlineKeyboardMarkup(keyboard), quote=True)


handlers = {
    "/start": start,
}

default_handler = on_text_input

callback_handlers = {
    encode_ascii_action: None,
    decode_binary: None,
    decode_hex: None,
}


def register_handlers(dp: Dispatcher):
    for command in handlers:
        dp.add_handler(MessageHandler(Filters.regex('^{}$'.format(command)), handlers[command]))
    dp.add_handler(MessageHandler(Filters.text, default_handler))
