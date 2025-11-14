# 🌾 Cambodia Soil Analyzer Bot

<div align="center">

![Cambodia Flag](https://img.shields.io/badge/Made%20for-Cambodia%20🇰🇭-red?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-4285F4?style=for-the-badge&logo=google)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered Telegram bot helping Cambodian farmers analyze soil and grow better crops.**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing)

</div>

---

## 📖 About

Cambodia Soil Analyzer is a free Telegram bot that uses AI to help farmers make better decisions about their crops. Simply send a photo of your soil, and get instant expert advice in Khmer or English.

### 🎯 Problem It Solves

- Farmers don't know their soil type
- Uncertainty about which crops to plant
- Wasting money on wrong fertilizers
- Language barriers (most tools are English-only)

### ✨ Solution

- **Instant Analysis**: Get soil analysis in seconds
- **Smart Recommendations**: AI suggests best crops for your soil
- **Cost Savings**: Know exactly which fertilizers to use
- **Bilingual**: Full support for Khmer and English
- **100% Free**: No subscription, no hidden costs

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 📸 **Photo Analysis** | Upload soil photo, get instant AI analysis |
| 🌱 **Crop Recommendations** | Best crops for your specific soil type |
| 💊 **Fertilizer Advice** | Exact fertilizers and application methods |
| 💰 **Cost Estimates** | Budget planning for fertilizers |
| 🇰🇭 **Khmer Language** | Full support for Cambodian farmers |
| 🇬🇧 **English Language** | International accessibility |
| 🤖 **AI-Powered** | Google Gemini 2.0 Flash (FREE) |
| ⚡ **Fast Results** | Analysis in 10-15 seconds |
| 🆓 **Completely Free** | No costs, no limits |

---

## 📸 Demo

### English Interface
```
🌾 Cambodia Soil Analyzer

Hi! I help farmers analyze soil and grow better crops.

📸 Send me a soil photo

I'll analyze:

🔹 Soil type & quality
🌱 Best crops for your soil
💊 Fertilizer recommendations
💰 Cost estimates

🆓 Free • ⚡ Fast • 🎯 Accurate

👇 Tap a button below to start!
```

### Khmer Interface
```
🌾 ប្រព័ន្ធវិភាគដីកម្ពុជា

សួស្តី! ខ្ញុំជួយកសិករវិភាគដី និងដាំដំណាំបានល្អជាងមុន។

📸 ផ្ញើរូបដីមកខ្ញុំ

ខ្ញុំនឹងវិភាគ:

🔹 ប្រភេទដី និងគុណភាព
🌱 ដំណាំល្អបំផុតសម្រាប់ដីអ្នក
💊 ដំបូន្មានអំពីជី
💰 ការប៉ាន់ស្មានតម្លៃ

🆓 ឥតគិតថ្លៃ • ⚡ លឿន • 🎯 ត្រឹមត្រូវ

👇 ចុចប៊ូតុងខាងក្រោមដើម្បីចាប់ផ្តើម!
```

---

## 🛠️ Installation

### Prerequisites

- Python 3.11 or higher
- Telegram account
- Google Gemini API key (FREE)

### Step 1: Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/cambodia-soil-analyzer.git
cd cambodia-soil-analyzer
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Get API Keys

#### Telegram Bot Token (FREE)
1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow instructions
3. Copy the bot token

#### Google Gemini API Key (FREE)
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Get API Key" → "Create API Key"
4. Copy the API key

### Step 5: Configure Environment

```bash
cp .env.example .env
```

Edit `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here
```

### Step 6: Run the Bot

```bash
python bot.py
```

You should see:
```
==================================================
🌾 Cambodia Soil Analyzer Bot
Version: 1.0
Status: Starting...
==================================================
```

---

## 🚀 Usage

### For Users

1. **Start the bot**: Search for your bot on Telegram and send `/start`
2. **Choose language**: Tap "🌐 Language / ភាសា" to switch between English and Khmer
3. **Send soil photo**: Tap "📸 Take Photo / ថតរូប" and send a clear photo of your soil
4. **Get results**: Wait 10-15 seconds for AI analysis
5. **Follow advice**: Use the recommendations to improve your farming

### For Developers

```python
# Import the analyzer
from soil_analyzer import analyze_soil_image

# Analyze soil
result = analyze_soil_image(image_bytes, language='en')
print(result)
```

---

## 🔄 Running 24/7

### Option 1: Systemd Service (Recommended for Linux)

The bot includes an auto-start service. Install it:

```bash
sudo cp cambodia-soil-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable cambodia-soil-bot.service
sudo systemctl start cambodia-soil-bot.service
```

Check status:
```bash
sudo systemctl status cambodia-soil-bot.service
```

View logs:
```bash
sudo journalctl -u cambodia-soil-bot.service -f
```

### Option 2: Quick Start Script

```bash
./start_bot.sh
```

### Option 3: Background Process

```bash
nohup python bot.py > bot_output.log 2>&1 &
```

### Option 4: Screen Session

```bash
screen -S soil-bot
python bot.py
# Press Ctrl+A then D to detach
```

---

## 📁 Project Structure

```
cambodia-soil-analyzer/
├── bot.py                          # Main bot application
├── soil_analyzer.py                # AI soil analysis logic
├── translations.py                 # Bilingual translations
├── config.py                       # Configuration loader
├── requirements.txt                # Python dependencies
├── .env                            # API keys (not in git)
├── .env.example                    # Example environment file
├── .gitignore                      # Git ignore rules
├── start_bot.sh                    # Quick start script
├── cambodia-soil-bot.service       # Systemd service file
├── AUTO_START_GUIDE.md             # Auto-start instructions
├── SETUP_COMPLETE.md               # Setup summary
└── README.md                       # This file
```

---

## 🧪 Technologies Used

- **Python 3.11+**: Core programming language
- **python-telegram-bot**: Telegram Bot API wrapper
- **Google Gemini 2.0 Flash**: AI for soil analysis
- **Pillow (PIL)**: Image processing
- **python-dotenv**: Environment variable management

---

## 💰 Cost Breakdown

| Service | Cost | Limits |
|---------|------|--------|
| Telegram Bot API | **FREE** | Unlimited |
| Google Gemini API | **FREE** | 15 requests/min, 1500/day |
| Hosting (Systemd) | **FREE** | Your own server |
| Total | **$0/month** | Perfect for small-medium usage |

---

## 🌍 Supported Soil Types

The bot recognizes 5 main Cambodian soil types:

1. **Sandy Soil** (ដីខ្សាច់) - Light, well-drained
2. **Red/Basaltic Soil** (ដីក្រហម) - Fertile, mineral-rich
3. **Clay/Alluvial Soil** (ដីឥដ្ឋ/ដីល្បាប់) - Best for rice
4. **Alluvial Mixed Soil** (ដីលាយ) - Good for vegetables
5. **Mountain Soil** (ដីភ្នំ) - Rocky, challenging

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Ideas for Contribution

- Add more languages (Thai, Vietnamese, Lao)
- Improve soil analysis accuracy
- Add weather integration
- Create mobile app version
- Add crop disease detection
- Improve UI/UX

---

## 🐛 Troubleshooting

### Bot not responding?

```bash
# Check if bot is running
systemctl status cambodia-soil-bot.service

# View logs
tail -f bot.log

# Restart bot
sudo systemctl restart cambodia-soil-bot.service
```

### API errors?

- Check if your API keys are correct in `.env`
- Verify Gemini API quota: [Google AI Studio](https://aistudio.google.com/)
- Check internet connection

### Image analysis fails?

- Ensure image is clear and well-lit
- Image should show soil texture clearly
- Try taking photo in daylight
- Maximum image size: 2048px

---

## 📝 License

This project is licensed under the MIT License.

**Copyright © 2024 Anachak Cyb3r**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

## 👨‍💻 Contributors

This project was built by:

### **Pring Rady** - Lead Developer
- GitHub: [@PringRady](https://github.com/PringRady)
- Role: Project Lead, Backend Development, AI Integration

### **Morn Chanthoung** - Developer
- GitHub: [@MornChanthoung](https://github.com/MornChanthoung)
- Role: Bot Development, Khmer Translation, Testing

### **Mi Lyheng** - Developer
- GitHub: [@MiLyheng](https://github.com/MiLyheng)
- Role: UI/UX Design, Documentation, Quality Assurance

---

## 🙏 Acknowledgments

- Google Gemini for free AI API
- Telegram for free bot platform
- Cambodian farmers for inspiration
- Open source community

---

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/YOUR_USERNAME/cambodia-soil-analyzer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/YOUR_USERNAME/cambodia-soil-analyzer/discussions)
- **Email**: your.email@example.com

---

<div align="center">

**Made with ❤️ for Cambodia's farmers 🌾🇰🇭**

If this project helps you, please give it a ⭐ on GitHub!

</div>
