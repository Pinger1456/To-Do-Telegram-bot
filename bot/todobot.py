"""
Telegram Bot to manage a simple To-Do List.
"""
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackContext
)

# Global list of tasks
TASKS = []


async def start(update: Update) -> None:
    """Sends a welcome message and instructions on the /start command."""
    await update.message.reply_text(
        'Hello! I am a task management bot. '
        'Use the /add <task> command to add a new task.'
    )


async def add_task(update: Update, context: CallbackContext) -> None:
    """Adds a task to the global task list."""
    if context.args:
        task = " ".join(context.args)
        TASKS.append(task)
        await update.message.reply_text(f'Task added: {task}')
    else:
        await update.message.reply_text(
            'Please provide a task description after the /add command.'
        )


async def list_tasks(update: Update) -> None:
    """Sends the user a list of all tasks."""
    if TASKS:
        task_list = "\n".join(
            f"{i + 1}. {task}" for i, task in enumerate(TASKS))
        await update.message.reply_text(f"Your tasks: \n{task_list}")
    else:
        await update.message.reply_text('No tasks yet.')


def main(token: str) -> None:
    """Starts the Telegram bot."""
    # Insert your bot token obtained
    application = Application.builder().token(token).build()

    # Register commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("add", add_task))
    application.add_handler(CommandHandler("list", list_tasks))

    # Run the bot
    application.run_polling()
