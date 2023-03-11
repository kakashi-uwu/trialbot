from telegram import ChatAction, InputMediaPhoto
from telegram.ext import CommandHandler, Updater

def start(update, context):
    context.bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.UPLOAD_PHOTO)
    context.bot.send_photo(chat_id=update.message.chat_id, photo='https://graph.org//file/7b263b04a2fe3559bd769.jpg')

updater = Updater('5790186855:AAGkEwBLRNW9Ync0JN6pzI9BJBaNpgtW_tw')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
