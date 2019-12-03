from telegram import Message, Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CallbackContext

import number_systems as ns

ACTION_DECODE_BINARY, ACTION_DECODE_EASY_BINARY, ACTION_DECODE_ASCII = \
    ("decode_binary", "decode_easy_binary", "decode_ascii")


def decode_binary(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    keyboard = [
        [
            InlineKeyboardButton("ASCII", callback_data=ACTION_DECODE_ASCII),
        ],
        [
            InlineKeyboardButton("просто бинарный текст", callback_data=ACTION_DECODE_EASY_BINARY)
        ]
    ]

    msg.edit_text("Текст был закодирован с помощью:", reply_markup=InlineKeyboardMarkup(keyboard))


def decode_binary_encoded_by(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    user_txt: str = reply_to.text
    user_txt = user_txt.replace(" ", "")

    text = ""
    if query.data == ACTION_DECODE_EASY_BINARY:
        text = ns.get_converter(ns.BINARY, ns.TEXT)(user_txt)
    elif query.data == ACTION_DECODE_ASCII:
        text = ns.get_converter(ns.ASCII, ns.TEXT)(user_txt)

    msg.edit_text(text)


button_callback_handlers = {
    ACTION_DECODE_ASCII: decode_binary_encoded_by,
    ACTION_DECODE_EASY_BINARY: decode_binary_encoded_by,
}