import re
import ascii
from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackQueryHandler
from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

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
        keyboard.append([InlineKeyboardButton("Перевести в ASCII", callback_data=str(encode_ascii_action))])

    if bool(re.fullmatch(BINARY_REGEX, message.text)):
        keyboard.append(([InlineKeyboardButton("Перевести из ASCII", callback_data=str(decode_binary))]))

    if bool(re.fullmatch(HEX_REGEX, message.text)):
        keyboard.append([InlineKeyboardButton("Перевести из 16-системы", callback_data=str(decode_hex))])

    message.reply_text("Доступные действия:", reply_markup=InlineKeyboardMarkup(keyboard), quote=True)


encode_by_pairing_action, encode_by_unpaired_action, ascii_encode_both_action = range(10, 13)


def encode_ascii(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    keyboard = [
        [
            InlineKeyboardButton("парности", callback_data=str(encode_by_pairing_action)),
            InlineKeyboardButton("непарности", callback_data=str(encode_by_unpaired_action)),
        ],
        [
            InlineKeyboardButton("парности и непарности", callback_data=str(ascii_encode_both_action))
        ]
    ]

    msg.edit_text("Перевести в ASCII по:", reply_markup=InlineKeyboardMarkup(keyboard))


def encode_ascii_by(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    if query.data == str(encode_by_pairing_action):
        txt = "ASCII парность:\n" + str(ascii.encode_by_pairing(ascii.text_to_binary(reply_to.text)))
    elif query.data == str(encode_by_unpaired_action):
        txt = "ASCII непарность:\n" + str(ascii.encode_by_unpaired(ascii.text_to_binary(reply_to.text)))
    else:
        txt = "ASCII парность:\n" + str(ascii.encode_by_pairing(ascii.text_to_binary(reply_to.text))) + \
              "\n\nASCII непарность:\n" + str(ascii.encode_by_unpaired(ascii.text_to_binary(reply_to.text)))

    msg.edit_text(txt)


decode_by_pairing_action, decode_by_unpaired_action = range(20, 22)


def decode_ascii(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    keyboard = [
        [
            InlineKeyboardButton("парности", callback_data=str(decode_by_pairing_action)),
            InlineKeyboardButton("непарности", callback_data=str(decode_by_unpaired_action)),
        ],
    ]

    msg.edit_text("Перевести из ASCII по:", reply_markup=InlineKeyboardMarkup(keyboard))


def decode_ascii_by(update: Update, context: CallbackContext):



handlers = {
    "/start": start,
}

default_handler = on_text_input

callback_handlers = {
    str(encode_ascii_action): encode_ascii,
    str(decode_binary): None,
    str(decode_hex): None,

    str(encode_by_pairing_action): encode_ascii_by,
    str(encode_by_unpaired_action): encode_ascii_by,
    str(ascii_encode_both_action): encode_ascii_by,

    str(decode_by_pairing_action): decode_ascii_by,
    str(decode_by_pairing_action): decode_ascii_by,
}


def register_handlers(dp: Dispatcher):
    for command in handlers:
        dp.add_handler(MessageHandler(Filters.regex('^{}$'.format(command)), handlers[command]))

    for pattern in callback_handlers:
        dp.add_handler(CallbackQueryHandler(callback_handlers[pattern], pattern=r"^{}$".format(pattern)))

    dp.add_handler(MessageHandler(Filters.text, default_handler))
