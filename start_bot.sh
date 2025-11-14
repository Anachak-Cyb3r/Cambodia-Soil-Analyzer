#!/bin/bash
# Cambodia Soil Analyzer Bot - Auto Start Script

cd "$(dirname "$0")"

# Activate virtual environment
source venv/bin/activate

# Start the bot
python bot.py
