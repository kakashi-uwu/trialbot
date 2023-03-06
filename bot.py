import telegram
from telegram.ext import Updater, CommandHandler


start_image="https://graph.org//file/7b263b04a2fe3559bd769.jpg"
# Replace YOUR_TOKEN_HERE with your actual Telegram bot token
bot = telegram.Bot(token='5792603393:AAEIi1EyAToI0bMNp5WkVXb7kdd7HLKCjNw')

def start(update, context):
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=open('start_image', 'rb'))

def main():
    updater = Updater(token='5792603393:AAEIi1EyAToI0bMNp5WkVXb7kdd7HLKCjNw', use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
