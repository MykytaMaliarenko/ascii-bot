from telegram.ext import Dispatcher, MessageHandler, Filters
from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext


def start(update: Update, context: CallbackContext):
    pass


handlers = {
    "/start": start,
}

default_handler = start


def register_handlers(dp: Dispatcher):
    for command in handlers:
        dp.add_handler(MessageHandler(Filters.regex('^{}$'.format(command)), handlers[command]))
    dp.add_handler(MessageHandler(Filters.text, default_handler))
