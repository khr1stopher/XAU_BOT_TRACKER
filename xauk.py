import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Configure logging
logging.basicConfig(
    level=logging.INFO
)
logger = logging.getLogger(__name__)

NOTIFICATION_CHAT_ID = "#1314320085"

# Replace with your actual bot token from BotFather
BOT_TOKEN = '7305250686:AAG82xgy2CngkQjMWyz8dnhbmLSg4eKUEus'

# The specific channel username (without the @ symbol)
CHANNEL_USERNAME = '𝑴𝒂𝒗𝒊𝒂__𝑭𝒙 𝑪𝒐𝒎𝒎𝒖𝒏𝒊𝒕𝒚 🐬'

# The specific signal/message you want to watch for
WATCH_SIGNAL = '#XAUUSD'

async def start(update: Update, context):
    """Handler for the /start command"""
    await update.message.reply_text('Channel signal monitoring bot is running!')

async def handle_channel_post(update: Update, context):
    """Handle incoming channel posts and check for the specific signal"""
    # Check if the post is from the specified channel
    if update.channel_post and update.channel_post.chat.username == CHANNEL_USERNAME:
        message_text = update.channel_post.text or ''
        
        # Check if the message contains the specific signal
        if WATCH_SIGNAL.lower() in message_text.lower():
            logger.info(f"Signal detected in channel {CHANNEL_USERNAME}")
            
            # Send a notification to the specified chat
            await context.bot.send_message(
                chat_id=NOTIFICATION_CHAT_ID, 
                text=f"Signal detected in {CHANNEL_USERNAME}: {message_text}"
            )

def main():
    """Main function to start the bot"""
    # Create the Application and pass your bot's token
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.ChatType.CHANNEL, handle_channel_post))
    
    # Start the bot
    logger.info("Channel monitoring bot started. Press Ctrl+C to stop.")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()