import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from constants import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Hi, how about a kniffel round?")

def unknown(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


def main():
  updater = Updater(token=TOKEN, use_context=True)

  dispatcher = updater.dispatcher

  start_handler = CommandHandler('start', start)
  dispatcher.add_handler(start_handler)

  unknown_handler = MessageHandler(Filters.command, unknown)
  dispatcher.add_handler(unknown_handler)

  updater.start_polling()

  updater.idle()

if __name__ == '__main__':
  main()
