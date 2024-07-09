import os
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Use environment variables for sensitive data
TOKEN = os.getenv('7453258851:AAHBn_uEs9gmCtjKN-MOKJOaeQnXdL85axk')
SOURCE_CHAT_ID = os.getenv('2206077017')
DESTINATION_CHAT_ID = os.getenv('2178408268')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def forward_message(update, context):
    """Forward messages from the source chat to the destination chat."""
    if update.message.chat_id == int(SOURCE_CHAT_ID):
        context.bot.forward_message(
            chat_id=DESTINATION_CHAT_ID,
            from_chat_id=update.message.chat_id,
            message_id=update.message.message_id
        )

def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, forward_message))
    dp.add_handler(MessageHandler(Filters.photo & ~Filters.command, forward_message))
    dp.add_handler(MessageHandler(Filters.video & ~Filters.command, forward_message))
    dp.add_handler(MessageHandler(Filters.document & ~Filters.command, forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
