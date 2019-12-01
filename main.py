import os
import json

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import handlers

ENV_FILE = "env.json"


def set_env():
    if os.path.isfile(ENV_FILE):
        with open(ENV_FILE, "r") as file:
            data = json.load(file)
            for key in data:
                os.environ[key] = data[key]


def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    set_env()
    updater = Updater(os.environ["BOT_TOKEN"], use_context=True)

    dp = updater.dispatcher

    handlers.register_handlers(dp)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
