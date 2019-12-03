from telegram import Message, Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CallbackContext

import number_systems as ns

ACTION_DECODE_BINARY, ACTION_DECODE_EASY_BINARY, ACTION_DECODE_ASCII, ACTION_ENCODE_TEXT_TO_HEX = \
    ("decode_binary", "decode_easy_binary", "decode_ascii", "decode_ascii_encode_text_to_hex")


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

    keyboard = [
        [
            InlineKeyboardButton("Перевести в 16-ричную систему", callback_data=ACTION_ENCODE_TEXT_TO_HEX),
        ],
    ]

    msg.edit_text(text)
    query.edit_message_reply_markup(InlineKeyboardMarkup(keyboard))


def encode_text_to_hex(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    msg_text: str = msg.text
    text = ns.get_converter(ns.TEXT, ns.HEX)(msg_text)

    msg.reply_text(text, quote=True)
    query.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup([]))


button_callback_handlers = {
    ACTION_DECODE_BINARY: decode_binary,
    ACTION_DECODE_ASCII: decode_binary_encoded_by,
    ACTION_DECODE_EASY_BINARY: decode_binary_encoded_by,
    ACTION_ENCODE_TEXT_TO_HEX: encode_text_to_hex,
}