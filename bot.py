import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton

START_IMG=("https://graph.org//file/8a091b6e8593e5def3c45.jpg")

PM_START_TEXT = """
Hey guys I'm ichigo, see am back...\n
*I'll be ready soon rn I'm under maintenance hehe.......* 
──『*Launching soon..*』
"""



def start(update, context):
    update.effective_message.reply_photo(
     START_IMG,
     PM_START_TEXT)

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
