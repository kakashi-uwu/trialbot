import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = '5792603393:AAEIi1EyAToI0bMNp5WkVXb7kdd7HLKCjNw'

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello, I'm a bot!")

def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
