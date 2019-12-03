from telegram import Message, Update, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from telegram.ext import CallbackContext

import number_systems as ns

ACTION_ENCODE_ASCII, ACTION_ENCODE_ASCII_BY_PAIRED, ACTION_ENCODE_ASCII_BY_UNPAIRED, ACTION_ENCODE_ASCII_BY_BOTH = \
    ("encode_ascii", "encode_ascii_by_pair", "encode_ascii_by_unpaired", "encode_ascii_by_both")


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

    msg.edit_text(txt)


button_callback_handlers = {
    ACTION_ENCODE_ASCII_BY_PAIRED: encode_ascii_by,
    ACTION_ENCODE_ASCII_BY_UNPAIRED: encode_ascii_by,
    ACTION_ENCODE_ASCII_BY_BOTH: encode_ascii_by,
}
