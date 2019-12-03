from telegram import Update, CallbackQuery, Message, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

import number_systems as ns

ACTION_DECODE_HEX, ACTION_DECODE_ASCII = ("decode_hex", "decode_hex_from_ascii_to_text")


def decode_hex(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message
    reply_to: Message = msg.reply_to_message

    user_txt: str = reply_to.text
    user_txt = user_txt.replace(" ", "")

    keyboard = [
        [
            InlineKeyboardButton("Перевести в текст", callback_data=ACTION_DECODE_ASCII),
        ],
    ]

    msg.edit_text("ASCII:\n{}".format(ns.get_converter(ns.HEX, ns.ASCII)(user_txt)),
                  reply_markup=InlineKeyboardMarkup(keyboard))


def decode_binary(update: Update, context: CallbackContext):
    query: CallbackQuery = update.callback_query
    msg: Message = query.message

    user_txt: str = msg.text
    user_txt = user_txt.replace(" ", "")

    msg.edit_reply_markup(reply_markup=InlineKeyboardMarkup([]))
    msg.reply_text(ns.get_converter(ns.ASCII, ns.TEXT)(user_txt), quote=True)


button_callback_handlers = {
    ACTION_DECODE_ASCII: decode_binary,
}
