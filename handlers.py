import re
from number_systems import MyBinary, MyASCII, MyHex
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


def on_text_input(update: Update, context: CallbackContext):
    message: Message = update.message

    keyboard = []
    if bool(re.fullmatch(r"[A-z]", message.text)):
        keyboard.append([InlineKeyboardButton("Перевести в ASCII", callback_data=str(encode_ascii_action))])

    if MyBinary.is_binary(message.text):
        keyboard.append(([InlineKeyboardButton("Перевести из ASCII", callback_data=str(decode_binary))]))

    if MyHex.is_hex(message.text):
        keyboard.append([InlineKeyboardButton("Перевести из 16-системы", callback_data=str(decode_hex))])

    message.reply_text("Доступные действия:", reply_markup=InlineKeyboardMarkup(keyboard), quote=True)


encode_by_pairing_action, encode_by_unpaired_action, ascii_encode_both_action = range(10, 13)


def on_encode_ascii(update: Update, context: CallbackContext):
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


def on_encode_ascii_by(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    user_txt = reply_to.text
    if query.data == str(encode_by_pairing_action):
        txt = "ASCII парность:\n" + MyASCII(text=user_txt).to_str_by_pairing()
    elif query.data == str(encode_by_unpaired_action):
        txt = "ASCII непарность:\n" + MyASCII(text=user_txt).to_str_by_unpaired()
    else:
        txt = "ASCII парность:\n" + MyASCII(text=user_txt).to_str_by_pairing() + \
              "\n\nASCII непарность:\n" + MyASCII(text=user_txt).to_str_by_unpaired()

    msg.edit_text(txt)


decode_encoded_by_ascii, decode_encoded_by_binary = range(20, 22)


def on_decode_ascii(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    keyboard = [
        [
            InlineKeyboardButton("ASCII", callback_data=str(decode_encoded_by_ascii)),
        ],
        [
            InlineKeyboardButton("просто бинарный текст", callback_data=str(decode_encoded_by_binary))
        ]
    ]

    msg.edit_text("Текст был закодирован с помощтю:", reply_markup=InlineKeyboardMarkup(keyboard))




handlers = {
    "/start": start,
}

default_handler = on_text_input

callback_handlers = {
    str(encode_ascii_action): on_encode_ascii,
    str(decode_binary): on_decode_ascii,
    str(decode_hex): None,

    str(encode_by_pairing_action): on_encode_ascii_by,
    str(encode_by_unpaired_action): on_encode_ascii_by,
    str(ascii_encode_both_action): on_encode_ascii_by,
}


def register_handlers(dp: Dispatcher):
    for command in handlers:
        dp.add_handler(MessageHandler(Filters.regex('^{}$'.format(command)), handlers[command]))

    for pattern in callback_handlers:
        dp.add_handler(CallbackQueryHandler(callback_handlers[pattern], pattern=r"^{}$".format(pattern)))

    dp.add_handler(MessageHandler(Filters.text, default_handler))
