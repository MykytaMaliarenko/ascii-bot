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


encode_ascii_action, decode_binary, decode_hex, encode_hex = range(4)


def on_text_input(update: Update, context: CallbackContext):
    message: Message = update.message

    keyboard = []
    if bool(re.fullmatch(r'^[!@#$%^&*(),.?":{};|<>№A-z0-9\s]+$', message.text)):
        keyboard.append([InlineKeyboardButton("Перевести в ASCII", callback_data=str(encode_ascii_action))])
        keyboard.append([InlineKeyboardButton("Перевести в 16-систему", callback_data=str(encode_hex))])

    if MyBinary.is_binary(message.text):
        keyboard.append(([InlineKeyboardButton("Перевести из 2-ичной системы", callback_data=str(decode_binary))]))

    if MyHex.is_hex(message.text):
        keyboard.append([InlineKeyboardButton("Перевести из 16-ичной системы", callback_data=str(decode_hex))])

    if len(keyboard) != 0:
        message.reply_text("Доступные действия:", reply_markup=InlineKeyboardMarkup(keyboard), quote=True)
    else:
        message.reply_text("Нету доступных действий ( текст должен быть написан латин. буквами):", quote=True)


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


def on_encode_hex(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    user_txt = reply_to.text
    txt = MyHex(MyBinary(text=user_txt)).to_hex_text()
    msg.edit_text(txt)


def on_decode_hex(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    user_txt = reply_to.text
    txt = MyHex(hex_text=user_txt).binary.to_text()
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


def on_decode_ascii_by(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    user_txt = reply_to.text
    if query.data == str(decode_encoded_by_ascii):
        txt = MyASCII(binary_text=user_txt).binary.to_text()
    elif query.data == str(decode_encoded_by_binary):
        txt = MyBinary(binary_text=user_txt).to_text()

    msg.edit_text(txt)


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

    str(decode_encoded_by_ascii): on_decode_ascii_by,
    str(decode_encoded_by_binary): on_decode_ascii_by,

    str(encode_hex): on_encode_hex,

    str(decode_hex): on_decode_hex,
}


def register_handlers(dp: Dispatcher):
    for command in handlers:
        dp.add_handler(MessageHandler(Filters.regex('^{}$'.format(command)), handlers[command]))

    for pattern in callback_handlers:
        dp.add_handler(CallbackQueryHandler(callback_handlers[pattern], pattern=r"^{}$".format(pattern)))

    dp.add_handler(MessageHandler(Filters.text, default_handler))
