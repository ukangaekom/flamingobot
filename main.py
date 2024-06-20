import asyncio
from typing import Final
from telegram import Update,ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext
# from dotenv import load_dotenv
# import os
import cryptoapi

# from cryptoapi import as neo


# loading .env file 
# load_dotenv()
# token = os.getenv("TOKEN")
# bot_username = os.getenv("BOT_NAME")
# TOKEN: Final = "7044426031:AAEQXanUICgzCPa_cHdVbG7bDpEz204wIQ"
TOKEN: Final = "7139508330:AAF51Jl1VZCPxRy5T6lVcU__XWUTyDPEdHo"
# BOT_USERNAME: Final = "@NeoCoachbot"
BOT_USERNAME: Final = "@flmneo_bot"
# bot = telebot.TeleBot("7139508330:AAF51Jl1VZCPxRy5T6lVcU__XWUTyDPEdHo")


# print(TOKEN, BOT_USERNAMEL)


# using async await to create bot functions

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello Welcome to flamingo help desk. Reply /help'
                                    'to know more about flamingo services')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('🕵️:I am flamingohelp bot and I have the following commands documentaions')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command')


async def getWalletDetails_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # markup = types.InlineKeyboardMarkup(row_width=2)
    # wallet = 'NYAN6Nfd5rNWqJhqz6KxXBDJSv1DtMHU9G'
    wallet: str = update.message.text
    wallet: str = wallet.split()
    wallet_address = wallet[1].strip()
    reply = cryptoapi.getWalletCoinBalance(wallet_address)
    walletTotal = cryptoapi.calculateWalletBalance(wallet_address)
    await update.message.reply_text(
        f"*Your Wallet Details* \n\n  {reply} \n *Balance:* 💰${walletTotal} \n *https://flamingo.finance*",
        parse_mode='Markdown')


async def getCoinDetails_comand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coin: str = update.message.text
    coin: str = coin.split()
    coin = coin[1].strip()
    currentPrice = cryptoapi.getLatestCoinPrice(coin)
    await update.message.reply_text(f'*💶Current Price* \n {currentPrice}', parse_mode="Markdown")


async def marketCap_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    flm_marketcap = cryptoapi.getFlamingoMarketCap()
    await update.message.reply_text(f'*Flamingo Market Cap* \n\n 📊*value*: *${flm_marketcap}*', parse_mode='Markdown')


async def getMarket_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # market = cryptoapi.getMarketData([cryptoapi.hash_coin[i] for i in cryptoapi.hash_coin])
    market_report = ''
    for i in market:
        market_report += '{i} coin'

    # await update.message.reply_text(f'{}')


# More commands can be written below


# Handling responses
def handle_response(text: str) -> str:
    processed: str = text.lower()
    if 'hi' in processed:
        return 'Hey There! I am flamingobot you need some help? send /help'

    return 'I dont know what you are talking about, sorry!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({Update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return

    else:
        response: str = handle_response(text)

    # print('BOT', response)
    await update.message.reply_text('{response}')


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} cause error {context.error}')



async def useMenu(update:Update, context: CallbackContext):

    keyboard = [[InlineKeyboardButton('MarketCap', callback_data='marketcap'),InlineKeyboardButton('Analysis', callback_data ='analysis_report')],
                [InlineKeyboardButton('About', callback_data='about_flamingo')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(text='*Choose the Following Button Options:*',reply_markup=reply_markup,parse_mode='Markdown')

def button_commands(update:Update, context: ContextTypes.DEFAULT_TYPE):
    """Handling all related button callbak query"""

    query = update.callback_query
    query.answer()

    if query.data == 'marketcap':
        print('hello world')
        # query.edit_message_text(text='You picked the marketcap options')






if __name__ == '__main__':
    print('Program is starting')
    # cryptoapi.getWalletCoinBalance('NYAN6Nfd5rNWqJhqz6KxXBDJSv1DtMHU9G')
    # cryptoapi.calculateWalletBalance('NYAN6Nfd5rNWqJhqz6KxXBDJSv1DtMHU9G')
    app = Application.builder().token(TOKEN).build()


    # command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('walletDetails', getWalletDetails_command))
    app.add_handler(CommandHandler('coinPrice', getCoinDetails_comand))
    app.add_handler(CommandHandler('marketcap', marketCap_command))
    app.add_handler(CommandHandler('options', useMenu))


    # print(dir(CallbackQueryHandler))
    # Adding callback queries
    # button = CallbackQueryHandler('marketcap',marketCap_command)
    app.add_handler(CallbackQueryHandler('marketcap',button_commands(Update,CallbackContext)))

    #  message handlers
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # error
    app.add_error_handler(error)

    # Printing polling
    print('polling ....')
    app.run_polling(poll_interval=3)
