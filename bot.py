import os
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton

START_IMG=("https://graph.org//file/7b263b04a2fe3559bd769.jpg")

PM_START_TEXT = """
hello vro
"""


def start(update, context):
      first_name = update.effective_user.first_name
            update.effective_message.reply_photo(
                START_IMG,
                PM_START_TEXT.format(
                    escape_markdown(first_name), escape_markdown(context.bot.first_name),
                ),
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="☑️ Add me",
                                url="t.me/{}?startgroup=true".format(
                                    context.bot.username,
                                ),
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="🚑 Support",
                                url=f"https://t.me/{SUPPORT_CHAT}",
                            ),
                            InlineKeyboardButton(
                                text="🔔 Updates",
                                url="https://t.me/OnePunchUpdates",
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="🧾 Getting Started",
                                url="https://t.me/OnePunchUpdates/29",
                            ),
                            InlineKeyboardButton(
                                text="🗄 Source code",
                                url="https://github.com/AnimeKaizoku/SaitamaRobot",
                            ),
                        ],
                        [
                            InlineKeyboardButton(
                                text="☠️ Kaizoku Network",
                                url="https://t.me/Kaizoku/4",
                            ),
                        ],
                    ],
                ),
            )
    else:
        update.effective_message.reply_text(
            "I'm awake already!\n<b>Haven't slept since:</b> <code>{}</code>".format(
                uptime,
            ),
            parse_mode=ParseMode.HTML,
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
