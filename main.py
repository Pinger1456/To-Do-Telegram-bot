"""
Telegram Bot to manage a simple To-Do List.
"""

from bot import todobot
from config import TOKEN

if __name__ == '__main__':
    if TOKEN is None:
        raise ValueError(
            "Please set TELEGRAM_BOT_TOKEN in your .env file.")
    todobot.main(TOKEN)
