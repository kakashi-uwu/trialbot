from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import random

# Telegram Bot API Token
TOKEN = '5063237105:AAHGFmZ1RFNhil9xo0oeLDPYc_TULjAWxNM'

# URL to fetch waifus from
WAIFU_URL = 'https://api.waifu.pics/sfw/waifu'

# Define a function to handle the /start command
def start(update, context):
    update.message.reply_text('Welcome to the Waifu Catcher bot!')

# Define a function to handle the /catch command
def catch(update, context):
    # Fetch a random waifu image
    response = requests.get(WAIFU_URL)
    waifu_url = response.json()['url']

    # Send the waifu image to the user
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=waifu_url)

# Define a function to handle messages
def message_handler(update, context):
    # Parse the message text
    text = update.message.text.lower()

    # Check if the message contains the word "waifu"
    if 'waifu' in text:
        # Fetch a random waifu image
        response = requests.get(WAIFU_URL)
        waifu_url = response.json()['url']

        # Send the waifu image to the user
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=waifu_url)
    else:
        # Send a generic response
        update.message.reply_text('Sorry, I didn\'t understand that command.')

# Create the bot and add handlers
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('catch', catch))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

# Start the bot
updater.start_polling()
