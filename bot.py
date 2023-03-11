import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton

START_IMG=("https://graph.org//file/7b263b04a2fe3559bd769.jpg")

PM_START_TEXT = """
hello vro
"""


def start(update, context):
          update.effective_message.reply_photo(
               random.choice(START_IMG),PM_START_TEXT,
                timeout=60,
            )
    
def main():
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print('Error: Please set the BOT_TOKEN environment variable.')
        return

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()

if __name__ == '__main__':
    main()
