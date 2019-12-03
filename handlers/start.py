from telegram.update import Update, Message
from telegram.ext.callbackcontext import CallbackContext

GREETING = "Привет!\nЯ могу переводить текст в ascii код по парности и непарности " \
           ", а так же переводить его в 16-ричну систему.\nПросто напиши что-то " \
           "и я покажу все доступные действия.\n\nАвтор: @Zikim"


def start(update: Update, context: CallbackContext):
    message: Message = update.message
    message.reply_text(GREETING)
