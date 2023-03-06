import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm a bot.")

def main():
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print('Error: Please set the BOT_TOKEN environment variable.')
        return
    
 def handle_message(update, context):
    text = update.message.text
    if text == '/gstart':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! Type /game to play my game.")
    elif text == '/game':
        # start the game here
        context.bot.send_message(chat_id=update.effective_chat.id, text="Let's play my game!")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm sorry, I don't understand that command.")

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    updater.start_polling()

if __name__ == '__main__':
    main()
