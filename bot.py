import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton

START_IMG=("https://graph.org//file/e500a5e4524c6cad31096.png")

PM_START_TEXT = """
Hey user I'm *Ichigo* my working structure is still on update...\n
*Updating.......* 
──『*Be patient we'll be back soon*』
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
