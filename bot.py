import logging
import os
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ApplicationBuilder, MessageHandler, filters
from dotenv import load_dotenv

from exchange import convert_currency_erapi

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

async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    convertion = context.args
    logging.info(convertion)
    last_updated_datetime, exchange_rate = convert_currency_erapi(*convertion)
    print(exchange_rate)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=(f"{convertion[2]} {convertion[0]} = {exchange_rate} {convertion[1]}"))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    convert_handler = CommandHandler('convert', convert)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(convert_handler)
    application.run_polling()
