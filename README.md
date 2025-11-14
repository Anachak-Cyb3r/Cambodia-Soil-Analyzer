# 🌾 Cambodia Soil Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-Latest-blue.svg)
![License](https://img.shields.io/badge/License-Anachak%20Cyb3r-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![AI](https://img.shields.io/badge/AI-Google%20Gemini-4285F4.svg)

**An AI-powered Telegram bot helping Cambodian farmers analyze soil and grow better crops**

[Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage) • [Contributing](#-contributing) • [Team](#-contributors)

</div>

---

## 🌾 Overview

**Cambodia Soil Analyzer** is an intelligent Telegram bot developed by the **Anachak Cyb3r Team** to revolutionize farming in Cambodia. Our mission is to provide farmers with accessible AI-powered tools that help them make informed decisions about soil quality, crop selection, and fertilizer usage.

This bot uses advanced AI technology to analyze soil photos and provide instant, expert recommendations in both Khmer and English, making agricultural knowledge accessible to all Cambodian farmers.

---

## 🌟 Key Features

| Feature | Description |
|---------|-------------|
| 📸 **Soil Photo Analysis** | Upload a soil photo and get instant AI-powered analysis |
| 🔍 **Soil Type Detection** | Identifies 5 main Cambodian soil types with quality ratings |
| 🌱 **Crop Recommendations** | Suggests best crops for your specific soil type |
| 💊 **Fertilizer Advice** | Recommends exact fertilizers and application methods |
| 💰 **Cost Estimates** | Provides budget planning for fertilizers per hectare |
| 🇰🇭 **Khmer Language** | Full support for Cambodian farmers |
| 🇬🇧 **English Language** | International accessibility |
| ⚡ **Fast Results** | Analysis completed in 10-15 seconds |
| 🆓 **100% Free** | No subscription, no hidden costs |

---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Google Gemini API Key (FREE from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Anachak-Cyb3r/Cambodia-Soil-Analyzer.git
   cd Cambodia-Soil-Analyzer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your API keys:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the bot**
   ```bash
   python bot.py
   ```

---

## 📖 Usage

### Starting the Bot

1. Open Telegram and search for your bot
2. Send `/start` command
3. Select your preferred language (Khmer 🇰🇭 or English 🇬🇧)
4. Tap "📸 Take Photo / ថតរូប" button
5. Send a clear photo of your soil
6. Wait 10-15 seconds for AI analysis
7. Receive detailed recommendations

### Available Commands

- `/start` - Initialize the bot and display main menu
- `/help` - Get usage instructions
- `/language` - Change language preference
- `/about` - Learn about the bot

### Supported Soil Types

The bot recognizes 5 main Cambodian soil types:

1. **Sandy Soil** (ដីខ្សាច់) - Light, well-drained
2. **Red/Basaltic Soil** (ដីក្រហម) - Fertile, mineral-rich
3. **Clay/Alluvial Soil** (ដីឥដ្ឋ/ដីល្បាប់) - Best for rice
4. **Alluvial Mixed Soil** (ដីលាយ) - Good for vegetables
5. **Mountain Soil** (ដីភ្នំ) - Rocky, challenging

---

## 🛠️ Technology Stack

- **Language:** Python 3.11+
- **Framework:** python-telegram-bot
- **AI Engine:** Google Gemini 2.0 Flash (FREE)
- **Image Processing:** Pillow (PIL)
- **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
Cambodia-Soil-Analyzer/
├── bot.py                          # Main bot application
├── soil_analyzer.py                # AI soil analysis logic
├── translations.py                 # Bilingual translations (Khmer/English)
├── config.py                       # Configuration loader
├── requirements.txt                # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── start_bot.sh                    # Quick start script
├── cambodia-soil-bot.service       # Systemd service for auto-start
├── AUTO_START_GUIDE.md             # Auto-start instructions
├── SETUP_COMPLETE.md               # Setup summary
├── LICENSE                         # License file
└── README.md                       # Project documentation
```

---

## 🔄 Running 24/7

### Option 1: Systemd Service (Recommended for Linux)

```bash
# Install service
sudo cp cambodia-soil-bot.service /etc/systemd/system/
sudo systemctl daemon-reload

# Enable auto-start on boot
sudo systemctl enable cambodia-soil-bot.service

# Start the service
sudo systemctl start cambodia-soil-bot.service

# Check status
sudo systemctl status cambodia-soil-bot.service
```

### Option 2: Quick Start Script

```bash
./start_bot.sh
```

### Option 3: Background Process

```bash
nohup python bot.py > bot_output.log 2>&1 &
```

For detailed instructions, see [AUTO_START_GUIDE.md](AUTO_START_GUIDE.md)

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Test your changes before submitting
- Update documentation as needed
- Ensure bilingual support (Khmer & English)

---

## 🧠 Our Mission

To make farming **smarter, easier, and more sustainable** by combining **AI and agriculture** — building a better future for Cambodian farmers through accessible technology and innovation.

---

## 👨‍💻 Contributors

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/identicons/1.png" width="100px;" alt=""/>
      <br />
      <sub><b>Pring Rady</b></sub>
      <br />
      <sub>Lead Developer</sub>
    </td>
    <td align="center">
      <img src="https://github.com/identicons/2.png" width="100px;" alt=""/>
      <br />
      <sub><b>Morn Chanthoung</b></sub>
      <br />
      <sub>Developer</sub>
    </td>
    <td align="center">
      <img src="https://github.com/identicons/3.png" width="100px;" alt=""/>
      <br />
      <sub><b>Mi Lyheng</b></sub>
      <br />
      <sub>Developer</sub>
    </td>
  </tr>
</table>

---

## 💰 Cost Breakdown

| Service | Cost | Limits |
|---------|------|--------|
| Telegram Bot API | **FREE** | Unlimited |
| Google Gemini API | **FREE** | 15 requests/min, 1500/day |
| Hosting (Self-hosted) | **FREE** | Your own server |
| **Total** | **$0/month** | Perfect for farmers |

---

## 📞 Support

For support, questions, or feedback:
- Open an issue on [GitHub Issues](https://github.com/Anachak-Cyb3r/Cambodia-Soil-Analyzer/issues)
- Contact the Anachak Cyb3r Team

---

## 📜 License

This project is licensed under **Anachak Cyb3r**.  
All rights reserved © 2024-2025.

**Copyright © 2024-2025 Anachak Cyb3r. All Rights Reserved.**

This software and associated documentation files are the proprietary property of Anachak Cyb3r. Unauthorized copying, modification, distribution, or use of this software, via any medium, is strictly prohibited without explicit written permission from Anachak Cyb3r.

---

## 🙏 Acknowledgments

- Thanks to all Cambodian farmers who inspired this project
- Google Gemini for providing free AI API
- Telegram Bot API for the platform
- The open-source community for their invaluable tools

---

<div align="center">

**Made with ❤️ by Anachak Cyb3r Team**

⭐ Star this repository if you find it helpful!

[🌾 Visit Our Main Project](https://github.com/Anachak-Cyb3r/Anachak-Kasekor-Chatbot)

</div>
