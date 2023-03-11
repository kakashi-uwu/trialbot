import telegram
from telegram.ext import (
    CallbackContext,
    CallbackQueryHandler,
    CommandHandler,
    Filters,
    MessageHandler,)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
TOKEN = '5790186855:AAGkEwBLRNW9Ync0JN6pzI9BJBaNpgtW_tw'

START_IMG=("https://graph.org//file/7b263b04a2fe3559bd769.jpg")

PM_START_TEXT = """
    ► *{}* ◄
Kon'nichiwa I'm *NISHI* I've got a lot of abilities to help you...\n
*JOIN OUR* -
[UPDATE CHANNEL](t.me/notyourishanymore) - [SUPPORTCHAT](t.me/notyourishanymore)\n
──『*ᴛʜᴀɴᴋs  ғᴏʀ  ᴜsɪɴɢ*』
"""

buttons = [
    [
        InlineKeyboardButton(
                            text="summon me",
                            url="t.me/elevatedrobot?startgroup=true"),
                    ],
                   [
                       InlineKeyboardButton(text="help and commands ?", callback_data="help_back"),
                       InlineKeyboardButton(text="about me", callback_data="vegeta_"
         ),
    ],
] 

def start(update: Update, context: CallbackContext):
    args = context.args
    uptime = get_readable_time((time.time() - StartTime))
    if update.effective_chat.type == "private":
        if len(args) >= 1:
            if args[0].lower() == "help":
                send_help(update.effective_chat.id, HELP_STRINGS)
            elif args[0].lower().startswith("ghelp_"):
                mod = args[0].lower().split("_", 1)[1]
                if not HELPABLE.get(mod, False):
                    return
                send_help(
                    update.effective_chat.id,
                    HELPABLE[mod].__help__,
                    InlineKeyboardMarkup(
                        [[InlineKeyboardButton(text="⬅Back", callback_data="help_back")]]
                    ),
                )

            elif args[0].lower().startswith("stngs_"):
                match = re.match("stngs_(.*)", args[0].lower())
                chat = dispatcher.bot.getChat(match.group(1))

                if is_user_admin(chat, update.effective_user.id):
                    send_settings(match.group(1), update.effective_user.id, False)
                else:
                    send_settings(match.group(1), update.effective_user.id, True)

            elif args[0][1:].isdigit() and "rules" in IMPORTED:
                IMPORTED["rules"].send_rules(update, args[0], from_pm=True)

        else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_photo(
               random.choice(START_IMG),PM_START_TEXT.format(first_name),
                reply_markup=InlineKeyboardMarkup(buttons),
                parse_mode=ParseMode.MARKDOWN,
                timeout=60,
            )
    else:
        first_name = update.effective_user.first_name
        update.effective_message.reply_animation(
            GROUPSTART_IMG, caption= "*hello!\n ┗► {} ◄┛,*\n*I'm BRUHa*\n*Haven't slept since* : {} ".format(
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


def echo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text=update.message.text)

def main():
    updater = Update(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
