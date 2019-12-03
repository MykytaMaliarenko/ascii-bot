from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackQueryHandler
from .start import start

text_handlers = {
    "start": start,
}

button_callback_handlers = {}

default_handler = None


def register_handlers(dp: Dispatcher):
    for command in text_handlers:
        dp.add_handler(MessageHandler(Filters.regex('^/{}$'.format(command)), text_handlers[command]))

    for pattern in button_callback_handlers:
        dp.add_handler(CallbackQueryHandler(button_callback_handlers[pattern], pattern=r"^{}$".format(pattern)))

    dp.add_handler(MessageHandler(Filters.text, default_handler))
