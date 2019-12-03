import re

from telegram import Message, Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CallbackContext

import number_systems as ns

ACTION_ENCODE_ASCII, ACTION_ENCODE_ASCII_BY_PAIRED, ACTION_ENCODE_ASCII_BY_UNPAIRED, ACTION_ENCODE_ASCII_BY_BOTH, \
    ACTION_ENCODE_ASCII_TO_HEX = \
    ("encode_ascii", "encode_ascii_by_pair", "encode_ascii_by_unpaired", "encode_ascii_by_both", "encode_ascii_to_hex")


def encode_ascii(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    keyboard = [
        [
            InlineKeyboardButton("парности", callback_data=ACTION_ENCODE_ASCII_BY_PAIRED),
            InlineKeyboardButton("непарности", callback_data=ACTION_ENCODE_ASCII_BY_UNPAIRED),
        ],
        [
            InlineKeyboardButton("парности и непарности", callback_data=ACTION_ENCODE_ASCII_BY_BOTH)
        ]
    ]

    msg.edit_text("Перевести в ASCII по:", reply_markup=InlineKeyboardMarkup(keyboard))


def encode_ascii_by(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    converter = ns.get_converter(ns.TEXT, ns.ASCII)

    user_txt: str = reply_to.text
    user_txt = user_txt.replace(" ", "")
    if query.data == ACTION_ENCODE_ASCII_BY_PAIRED:
        txt = "ASCII парность:\n{}".format(converter(user_txt, mode=ns.BY_PAIRED))
    elif query.data == ACTION_ENCODE_ASCII_BY_UNPAIRED:
        txt = "ASCII непарность:\n{}".format(converter(user_txt, mode=ns.BY_UNPAIRED))
    else:
        txt = "ASCII парность:\n{}\n\nASCII непарность:\n{}".format(converter(user_txt, mode=ns.BY_PAIRED),
                                                                    converter(user_txt, mode=ns.BY_UNPAIRED))

    keyboard = [
        [
            InlineKeyboardButton("Перевести в 16-ричную систему", callback_data=ACTION_ENCODE_ASCII_TO_HEX),
        ],
    ]

    msg.edit_text(txt)
    query.edit_message_reply_markup(InlineKeyboardMarkup(keyboard))


def encode_ascii_to_hex(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    msg_text: str = msg.text

    rows = re.split(r":\n", msg_text)
    res = []
    for row in rows:
        m = re.match(r"([0-1]+\s?)+", row)
        if m is not None:
            res.append(m.group(0).replace("\n", ""))

    converter = ns.get_converter(ns.ASCII, ns.HEX)

    if len(res) == 2:
        pairing = converter(res[0])
        unpaired = converter(res[1])

        text = "ASCII парность(16):\n{}\n\nASCII непарность(16):\n{}".format(pairing, unpaired)
    else:
        if "парность" in msg_text.lower():
            text = "ASCII парность(16):\n{}".format(converter(res[0]))
        else:
            text = "ASCII непарность(16):\n{}".format(converter(res[0]))

    msg.reply_text(text, quote=True)
    msg.edit_reply_markup(reply_markup=InlineKeyboardMarkup([]))


button_callback_handlers = {
    ACTION_ENCODE_ASCII: encode_ascii,
    ACTION_ENCODE_ASCII_BY_PAIRED: encode_ascii_by,
    ACTION_ENCODE_ASCII_BY_UNPAIRED: encode_ascii_by,
    ACTION_ENCODE_ASCII_BY_BOTH: encode_ascii_by,
    ACTION_ENCODE_ASCII_TO_HEX: encode_ascii_to_hex,
}
