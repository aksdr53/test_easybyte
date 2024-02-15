import logging
import os
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = os.getenv('TOKEN')


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'am a bot please talk to me!")


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=('Список доступных команд:\n/help - список '
                                         'команд\n/start - приветствие\n'
                                         ' /conver - конвертировать валюту'))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)

    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()