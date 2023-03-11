import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
          first_name = update.effective_user.first_name
          update.effective_message.reply_photo(
               random.choice(START_IMG),PM_START_TEXT.format(first_name),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
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
