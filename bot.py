"""
Cambodia Soil Analyzer Telegram Bot
Professional bot for Cambodian farmers to analyze soil and get crop recommendations

Author: Your Name
Version: 1.0
"""
import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)
import config
from soil_analyzer import analyze_soil_image
from translations import get_text

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# User language preferences (in-memory storage)
user_languages = {}


def get_main_menu_keyboard(lang='en'):
    """
    Generate main menu keyboard with bilingual labels
    
    Args:
        lang (str): Language code ('en' or 'km')
    
    Returns:
        ReplyKeyboardMarkup: Telegram keyboard markup
    """
    # Bilingual buttons - same for all users
    keyboard = [
        [KeyboardButton('📸 Take Photo / ថតរូប'), KeyboardButton('❓ Help / ជំនួយ')],
        [KeyboardButton('🌐 Language / ភាសា'), KeyboardButton('ℹ️ About / អំពី')]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /start command - Welcome new users
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    user_id = update.effective_user.id
    
    logger.info(f"User {user_id} started the bot")
    
    # Check if user has already selected a language
    if user_id in user_languages:
        # User has language preference, show welcome
        lang = user_languages[user_id]
        await update.message.reply_text(
            get_text(lang, 'welcome'),
            reply_markup=get_main_menu_keyboard(lang)
        )
    else:
        # New user, show language selection first
        keyboard = [
            [KeyboardButton('🇬🇧 English')],
            [KeyboardButton('🇰🇭 ខ្មែរ')]
        ]
        reply_markup = ReplyKeyboardMarkup(
            keyboard, 
            one_time_keyboard=True, 
            resize_keyboard=True
        )
        
        await update.message.reply_text(
            '🌾 Welcome to Anachak Soil Analyzer!\n'
            '🌾 សូមស្វាគមន៍មកកាន់ប្រព័ន្ធវិភាគដីអនាចក្រ!\n\n'
            '🌐 Please choose your language:\n'
            '🌐 សូមជ្រើសរើសភាសា:',
            reply_markup=reply_markup
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /help command - Show usage instructions
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, 'en')
    
    await update.message.reply_text(
        get_text(lang, 'help'),
        reply_markup=get_main_menu_keyboard(lang)
    )


async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /about command - Show bot information
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, 'en')
    
    await update.message.reply_text(
        get_text(lang, 'about'),
        reply_markup=get_main_menu_keyboard(lang)
    )

async def language_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle /language command - Language selection menu
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    keyboard = [
        [KeyboardButton('🇬🇧 English')],
        [KeyboardButton('🇰🇭 ខ្មែរ')]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard, 
        one_time_keyboard=True, 
        resize_keyboard=True
    )
    
    await update.message.reply_text(
        '🌐 Choose language / ជ្រើសរើសភាសា:',
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle text messages - Process button presses and language selection
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    user_id = update.effective_user.id
    text = update.message.text
    lang = user_languages.get(user_id, 'en')
    
    # Language selection
    if text in ['🇬🇧 English', 'English 🇬🇧', 'English', 'english']:
        user_languages[user_id] = 'en'
        logger.info(f"User {user_id} changed language to English")
        # Show welcome message after language selection
        await update.message.reply_text(
            get_text('en', 'welcome'),
            reply_markup=get_main_menu_keyboard('en')
        )
    
    elif text in ['🇰🇭 ខ្មែរ', 'ខ្មែរ 🇰🇭', 'ខ្មែរ', 'khmer']:
        user_languages[user_id] = 'km'
        logger.info(f"User {user_id} changed language to Khmer")
        # Show welcome message after language selection
        await update.message.reply_text(
            get_text('km', 'welcome'),
            reply_markup=get_main_menu_keyboard('km')
        )
    
    # Menu button handlers - bilingual buttons
    elif '📸' in text and ('Take' in text or 'ថតរូប' in text):
        await update.message.reply_text(
            get_text(lang, 'send_photo'),
            reply_markup=get_main_menu_keyboard(lang)
        )
    
    elif '❓' in text and ('Help' in text or 'ជំនួយ' in text):
        await help_command(update, context)
    
    elif '🌐' in text and ('Language' in text or 'ភាសា' in text):
        await language_command(update, context)
    
    elif 'ℹ️' in text and ('About' in text or 'អំពី' in text):
        await about_command(update, context)
    
    # Default response
    else:
        await update.message.reply_text(
            get_text(lang, 'send_photo'),
            reply_markup=get_main_menu_keyboard(lang)
        )

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Handle photo messages - Analyze soil images
    
    Args:
        update: Telegram update object
        context: Callback context
    """
    user_id = update.effective_user.id
    lang = user_languages.get(user_id, 'en')
    
    try:
        # Send analyzing message
        await update.message.reply_text(
            get_text(lang, 'analyzing'),
            reply_markup=get_main_menu_keyboard(lang)
        )
        
        # Get the highest quality photo
        photo = update.message.photo[-1]
        file = await context.bot.get_file(photo.file_id)
        
        # Download photo as bytes
        photo_bytes = await file.download_as_bytearray()
        
        # Analyze soil using AI
        result = analyze_soil_image(bytes(photo_bytes), language=lang)
        
        # Telegram message limit is 4096 characters
        MAX_MESSAGE_LENGTH = 4000
        
        if len(result) > MAX_MESSAGE_LENGTH:
            # Split long messages into chunks
            chunks = [
                result[i:i+MAX_MESSAGE_LENGTH] 
                for i in range(0, len(result), MAX_MESSAGE_LENGTH)
            ]
            
            for i, chunk in enumerate(chunks):
                if i == len(chunks) - 1:
                    # Last chunk includes menu
                    await update.message.reply_text(
                        chunk,
                        reply_markup=get_main_menu_keyboard(lang)
                    )
                else:
                    await update.message.reply_text(chunk)
        else:
            # Send complete result with menu
            await update.message.reply_text(
                result,
                reply_markup=get_main_menu_keyboard(lang)
            )
        
        # Prompt for another analysis
        await update.message.reply_text(
            get_text(lang, 'analyze_another'),
            reply_markup=get_main_menu_keyboard(lang)
        )
        
        logger.info(f"Successfully analyzed soil for user {user_id} (language: {lang})")
        
    except Exception as e:
        logger.error(f"Error processing photo for user {user_id}: {e}", exc_info=True)
        await update.message.reply_text(
            get_text(lang, 'error'),
            reply_markup=get_main_menu_keyboard(lang)
        )

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Global error handler for the bot
    
    Args:
        update: Telegram update object
        context: Callback context with error information
    """
    logger.error(f"Update {update} caused error: {context.error}", exc_info=context.error)


def main():
    """
    Main function to initialize and start the bot
    """
    try:
        # Create application with bot token
        application = Application.builder().token(config.TELEGRAM_BOT_TOKEN).build()
        
        # Register command handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        application.add_handler(CommandHandler("about", about_command))
        application.add_handler(CommandHandler("language", language_command))
        
        # Register message handlers
        application.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
        )
        application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
        
        # Register error handler
        application.add_error_handler(error_handler)
        
        # Start bot
        logger.info("=" * 50)
        logger.info("🌾 Cambodia Soil Analyzer Bot")
        logger.info("Version: 1.0")
        logger.info("Status: Starting...")
        logger.info("=" * 50)
        
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        logger.critical(f"Failed to start bot: {e}", exc_info=True)
        raise


if __name__ == '__main__':
    main()
