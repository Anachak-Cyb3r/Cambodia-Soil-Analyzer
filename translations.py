"""
Translation Module for Cambodia Soil Analyzer Bot

Provides bilingual support for English and Khmer languages
"""

TRANSLATIONS = {
    'en': {
        'welcome': (
            "🌾 *Cambodia Soil Analyzer*\n\n"
            "Hi! I help farmers analyze soil and grow better crops.\n\n"
            "📸 *Send me a soil photo*\n\n"
            "I'll analyze:\n\n"
            "🔹 Soil type & quality\n"
            "🌱 Best crops for your soil\n"
            "💊 Fertilizer recommendations\n"
            "💰 Cost estimates\n\n"
            "🆓 Free • ⚡ Fast • 🎯 Accurate\n\n"
            "👇 *Tap a button below to start!*"
        ),
        'language_changed': '✅ Language changed to English\n\nNow you can send me a soil photo! 📸',
        'send_photo': (
            "📸 Take a clear photo of your soil:\n\n"
            "✅ Good lighting (daytime)\n"
            "✅ Close-up view\n"
            "✅ Show the soil texture\n\n"
            "Then send it to me! 👇"
        ),
        'analyzing': 'I will analyze based on the soil photo you sent 🔍\n⏳ Please wait 10-15 seconds...',
        'error': '❌ Sorry, something went wrong.\n\nPlease try again or send a clearer photo. 📸',
        'no_photo': '⚠️ Please send a photo of your soil.\n\nUse the 📸 button below!',
        'help': (
            "📖 HOW TO USE THIS BOT:\n\n"
            "1️⃣ Press the 📸 button\n"
            "2️⃣ Take a photo of your soil\n"
            "3️⃣ Send the photo to me\n"
            "4️⃣ Wait 10-15 seconds\n"
            "5️⃣ Get your results! 🌾\n\n"
            "💡 TIP: Take photos in good daylight for best results!\n\n"
            "🌐 Change language anytime using the button below."
        ),
        'about': (
            "ℹ️ ABOUT THIS BOT\n\n"
            "🤖 AI-powered soil analyzer\n"
            "🇰🇭 Made for Cambodian farmers\n"
            "🌾 Helps you grow better crops\n"
            "💰 Save money on fertilizers\n"
            "🆓 100% FREE to use\n\n"
            "🌱 Supports rice, vegetables, fruits, and cash crops\n\n"
            "Made with ❤️ for Cambodia's farmers"
        ),
        'analyze_another': '📸 Want to analyze another soil sample?\n\nJust send me another photo!'
    },
    'km': {
        'welcome': (
            "🌾 *ប្រព័ន្ធវិភាគដីកម្ពុជា*\n\n"
            "សួស្តី! ខ្ញុំជួយកសិករវិភាគដី និងដាំដំណាំបានល្អជាងមុន។\n\n"
            "📸 *ផ្ញើរូបដីមកខ្ញុំ*\n\n"
            "ខ្ញុំនឹងវិភាគ:\n\n"
            "🔹 ប្រភេទដី និងគុណភាព\n"
            "🌱 ដំណាំល្អបំផុតសម្រាប់ដីអ្នក\n"
            "💊 ដំបូន្មានអំពីជី\n"
            "💰 ការប៉ាន់ស្មានតម្លៃ\n\n"
            "🆓 ឥតគិតថ្លៃ • ⚡ លឿន • 🎯 ត្រឹមត្រូវ\n\n"
            "👇 *ចុចប៊ូតុងខាងក្រោមដើម្បីចាប់ផ្តើម!*"
        ),
        'language_changed': '✅ បានប្តូរភាសាជាខ្មែរ\n\nឥឡូវអ្នកអាចផ្ញើរូបភាពដីបានហើយ! 📸',
        'send_photo': (
            "📸 ថតរូបដីច្បាស់លាស់:\n\n"
            "✅ ពន្លឺល្អ (ពេលថ្ងៃ)\n"
            "✅ ថតជិតៗ\n"
            "✅ បង្ហាញសម្បុរដី\n\n"
            "រួចផ្ញើមកខ្ញុំ! 👇"
        ),
        'analyzing': 'ខ្ញុំសូមធ្វើការវិភាគផ្អែកតាមរូបដីដែលអ្នកផ្ញើអោយ 🔍\n⏳ សូមរង់ចាំ ១០-១៥ វិនាទី...',
        'error': '❌ សូមទោស មានបញ្ហា។\n\nសូមព្យាយាមម្តងទៀត ឬផ្ញើរូបភាពច្បាស់ជាងនេះ។ 📸',
        'no_photo': '⚠️ សូមផ្ញើរូបភាពដី។\n\nចុចប៊ូតុង 📸 ខាងក្រោម!',
        'help': (
            "📖 របៀបប្រើប្រាស់:\n\n"
            "១️⃣ ចុចប៊ូតុង 📸\n"
            "២️⃣ ថតរូបដីរបស់អ្នក\n"
            "៣️⃣ ផ្ញើរូបភាពមកខ្ញុំ\n"
            "៤️⃣ រង់ចាំ ១០-១៥ វិនាទី\n"
            "៥️⃣ ទទួលបានលទ្ធផល! 🌾\n\n"
            "💡 ជំនួយ: ថតរូបពេលថ្ងៃ ដើម្បីបានលទ្ធផលល្អ!\n\n"
            "🌐 ប្តូរភាសាបានគ្រប់ពេល ដោយចុចប៊ូតុងខាងក្រោម។"
        ),
        'about': (
            "ℹ️ អំពីប្រព័ន្ធនេះ\n\n"
            "🤖 ប្រើបច្ចេកវិទ្យា AI វិភាគដី\n"
            "🇰🇭 បង្កើតសម្រាប់កសិករកម្ពុជា\n"
            "🌾 ជួយអ្នកដាំដំណាំបានល្អ\n"
            "💰 សន្សំលុយលើជី\n"
            "🆓 ឥតគិតថ្លៃ 100%\n\n"
            "🌱 គាំទ្រ ស្រូវ បន្លែ ផ្លែឈើ និងដំណាំសាច់ប្រាក់\n\n"
            "បង្កើតដោយ ❤️ សម្រាប់កសិករកម្ពុជា"
        ),
        'analyze_another': '📸 ចង់វិភាគដីមួយទៀតទេ?\n\nគ្រាន់តែផ្ញើរូបភាពមកខ្ញុំ!'
    }
}

def get_text(lang, key):
    """
    Get translated text for a given language and key
    
    Args:
        lang (str): Language code ('en' or 'km')
        key (str): Translation key
    
    Returns:
        str: Translated text, defaults to English if not found
    """
    return TRANSLATIONS.get(lang, TRANSLATIONS['en']).get(
        key, 
        TRANSLATIONS['en'][key]
    )
