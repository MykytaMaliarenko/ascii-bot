from telegram.ext import Dispatcher, MessageHandler, Filters, CallbackQueryHandler

from .start import start
from .text_input import on_text_input
from .encode_ascii import button_callback_handlers as encode_ascii_button_callback_handlers
from .decode_binary import button_callback_handlers as decode_binary_button_callback_handlers
from .decode_hex import button_callback_handlers as decode_hex_button_callback_handlers

text_handlers = {
    "start": start,
}

button_callback_handlers = {}
button_callback_handlers.update(encode_ascii_button_callback_handlers)
button_callback_handlers.update(decode_binary_button_callback_handlers)
button_callback_handlers.update(decode_hex_button_callback_handlers)

default_handler = on_text_input


def register_handlers(dp: Dispatcher):
    for command in text_handlers:
        dp.add_handler(MessageHandler(Filters.regex('^/{}$'.format(command)), text_handlers[command]))

    for pattern in button_callback_handlers:
        dp.add_handler(CallbackQueryHandler(button_callback_handlers[pattern], pattern=r"^{}$".format(pattern)))

    dp.add_handler(MessageHandler(Filters.text, default_handler))
