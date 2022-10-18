from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from dotenv import load_dotenv
import os

load_dotenv()


updater = Updater(os.environ["TELEGRAM_API_TOKEN"], use_context=True)


def start(update: Update, context: CallbackContext):
    print("CHAT ID: "+str(update.message.chat_id))
    print("USER ID: "+str(update.message.from_user.id))
    print("USERNAME : "+str(update.message.from_user.username))
    update.message.reply_text("Welcome to AOS!")
    # update.message.sen





def help(update: Update, context: CallbackContext):
    update.message.reply_text("you need help?")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))


updater.start_polling()
