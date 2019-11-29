import re
from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext

GREETING = "Hi!\nI can encode text in ascii by pairing or unpairing " \
           "and convert it to hex system.\n Just write text and you " \
           "will see all available options.\n GL =)"

ASCII_REGEX = r"[?!\().\dA-z]+"


def start(update: Update, context: CallbackContext):
    message: Message = update.message
    message.reply_text(GREETING)


def text_input(update: Update, context: CallbackContext):
    message: Message = update.message




handlers = {
    "/start": start,
}

default_handler = text_input


def register_handlers(dp: Dispatcher):
    for command in handlers:
        dp.add_handler(MessageHandler(Filters.regex('^{}$'.format(command)), handlers[command]))
    dp.add_handler(MessageHandler(Filters.text, default_handler))
