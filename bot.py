import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai
import os

# Set up OpenAI API credentials
openai.api_key = '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'

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text='Hello! I am a language model chatbot. Send me a message and I will respond with some text.')

# Define a function to handle user messages
def message_handler(update, context):
    message_text = update.message.text
    response_text = generate_response(message_text)
    context.bot.send_message(chat_id=update.message.chat_id, text=response_text)

# Define a function to generate a response using OpenAI GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text

# Set up the Telegram bot and handlers
updater = Updater(token='6277512659:AAEQHQOMU5btoyDaz88Nl3z7oLiyV0y9YaY', use_context=True)
dispatcher = updater.dispatcher

# Add the command and message handlers
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, message_handler))

# Start the bot
updater.start_polling()
