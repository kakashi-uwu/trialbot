import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm a bot.")

def main():
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print('Error: Please set the BOT_TOKEN environment variable.')
        return
    
def welcome(update, context):
    message = "Welcome to our chat! Thanks for joining us."
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    welcome_handler = CommandHandler('welcome', welcome)
    dispatcher.add_handler(welcome_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
