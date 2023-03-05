import os
from telegram.ext import Updater, CommandHandler

START_PG="https://graph.org//file/7b263b04a2fe3559bd769.jpg"
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm a bot.")
    context.bot.send_photo(chat_id=update.message.chat_id, photo="START_PG")

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
