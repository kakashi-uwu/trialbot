import telebot

# Replace with your bot token
TOKEN = '5063237105:AAHGFmZ1RFNhil9xo0oeLDPYc_TULjAWxNM'

# Create a new bot instance using the token
bot = telebot.TeleBot(TOKEN)

# Define a command handler
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello, welcome to my bot!")

# Define a message handler
@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

# Start the bot
bot.polling()
