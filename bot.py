import os
from telegram.ext import Updater, CommandHandler

START_IMG="https://graph.org//file/7b263b04a2fe3559bd769.jpg"

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm a bot.")
    
def fstart(update, context):    
       first_name = update.effective_user.first_name
       update.effective_message.reply_animation(
            START_IMG, caption= "hey there im a trial bot".format(
             first_name,uptime
            ),
            parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
                [
                  [
                  InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url=f"https://telegram.dog/{SUPPORT_CHAT}"),
                  InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url=f"t.me/{UPDATES_CHANNEL}"),
                  ]
                ]
            ),
        )

def main():
    TOKEN = os.environ.get('BOT_TOKEN')
    if not TOKEN:
        print('Error: Please set the BOT_TOKEN environment variable.')
        return

    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    fstart_handler = CommandHandler("fstart", fstart)

    updater.start_polling()

if __name__ == '__main__':
    main()
