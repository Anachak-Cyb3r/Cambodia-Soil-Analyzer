# 🌾 Cambodia Soil Analyzer Bot - Auto Start Guide

## ✅ No Errors Found!
Your bot is working perfectly with no issues.

## 🗑️ Cleaned Up Files
Removed unnecessary files:
- BUG_CHECK_REPORT.md
- RUNTIME_TEST_REPORT.md
- CAMBODIA_SOIL_REFERENCE.md

---

## 🚀 How to Run Bot Forever (Auto-Start on Boot)

### Option 1: Quick Start (Manual)
Just double-click or run:
```bash
./start_bot.sh
```

### Option 2: Auto-Start on Boot (Systemd Service)

**Step 1:** Install the service
```bash
sudo cp cambodia-soil-bot.service /etc/systemd/system/
sudo systemctl daemon-reload
```

**Step 2:** Enable auto-start
```bash
sudo systemctl enable cambodia-soil-bot.service
```

**Step 3:** Start the service now
```bash
sudo systemctl start cambodia-soil-bot.service
```

**Check status:**
```bash
sudo systemctl status cambodia-soil-bot.service
```

**View logs:**
```bash
sudo journalctl -u cambodia-soil-bot.service -f
```

**Stop the service:**
```bash
sudo systemctl stop cambodia-soil-bot.service
```

**Disable auto-start:**
```bash
sudo systemctl disable cambodia-soil-bot.service
```

---

## 📁 Important Files (Don't Delete!)

### Core Files:
- `bot.py` - Main bot code
- `soil_analyzer.py` - AI soil analysis
- `translations.py` - English/Khmer translations
- `config.py` - Configuration loader
- `.env` - Your API keys (KEEP SECRET!)
- `requirements.txt` - Python dependencies

### Folders:
- `venv/` - Python virtual environment
- `__pycache__/` - Python cache (auto-generated)

### Scripts:
- `start_bot.sh` - Quick start script
- `cambodia-soil-bot.service` - Auto-start service

### Documentation:
- `README.md` - Project documentation
- `AUTO_START_GUIDE.md` - This file
- `.env.example` - Example environment file
- `.gitignore` - Git ignore rules
- `bot.log` - Bot activity logs

---

## 🎯 Quick Commands

**Start bot manually:**
```bash
./start_bot.sh
```

**Start bot in background:**
```bash
nohup ./start_bot.sh > bot_output.log 2>&1 &
```

**Check if bot is running:**
```bash
ps aux | grep bot.py
```

**Kill bot process:**
```bash
pkill -f bot.py
```

---

## 💡 Tips

1. **Keep .env file safe** - It contains your API keys
2. **Check bot.log** - For debugging issues
3. **Use systemd service** - Best for auto-start on boot
4. **Update bot** - Just edit files and restart service

---

## 🆘 Troubleshooting

**Bot not starting?**
- Check if API keys are in `.env` file
- Make sure virtual environment is activated
- Check logs: `tail -f bot.log`

**Service not working?**
- Check status: `sudo systemctl status cambodia-soil-bot.service`
- View logs: `sudo journalctl -u cambodia-soil-bot.service -f`
- Restart: `sudo systemctl restart cambodia-soil-bot.service`

---

Made with ❤️ for Cambodia's farmers 🌾
