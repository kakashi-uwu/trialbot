import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton

START_IMG=("https://graph.org//file/7b263b04a2fe3559bd769.jpg")

PM_START_TEXT = """
    ► *{}* ◄
Kon'nichiwa I'm *ichigo* I've got a lot of abilities to help you...\n
*JOIN OUR* -
[UPDATE CHANNEL](t.me/hnhbhay) - [SUPPORTCHAT](t.me/nvkjehgfk)\n
──『*ᴛʜᴀɴᴋs  ғᴏʀ  ᴜsɪɴɢ*』
"""

buttons = [
    [
        InlineKeyboardButton(
                            text="summon me",
                            url="t.me/hinataxrobot?startgroup=true"),
                    ],
                   [
                       InlineKeyboardButton(text="help and commands ?", callback_data="help_back"),
                       InlineKeyboardButton(text="about me", callback_data="vegeta_"
         ),
    ],
] 

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
