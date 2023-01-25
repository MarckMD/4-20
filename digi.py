import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler

products = {
    1: {"name": "Product 1", "price": 10.99},
    2: {"name": "Product 2", "price": 5.99},
    3: {"name": "Product 3", "price": 15.99},
    # add more products here
    20: {"name": "Product 20", "price": 20.99}
}

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Welcome to our digital shop! Type /shop to see our products.")

def shop(update, context):
    message = "Our products:\n"
    for product_id, product in products.items():
        message += "{}. {} - ${:.2f}\n".format(product_id, product['name'], product['price'])
        context.bot.send_message(chat_id=update.message.chat_id, text=message)

def purchase(update, context):
    product_id = int(update.message.text)
    if product_id in products:
        product = products[product_id]
        message = "You have selected {} for ${:.2f}.\n".format(product['name'], product['price'])
        message += "Please confirm your purchase by typing /confirm or cancel by typing /cancel"
        context.user_data["product_id"] = product_id
        context.bot.send_message(chat_id=update.message.chat_id, text=message)
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="Invalid product ID. Please try again.")

def confirm(update, context):
    if "product_id" in context.user_data:
        product_id = context.user_data["product_id"]
        product = products[product_id]
        message = "Thank you for your purchase of {} for ${:.2f}. Your digital product will be delivered shortly.".format(product['name'], product['price'])
        context.bot.send_message(chat_id=update.message.chat_id, text=message)
        del context.user_data["product_id"]
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="No product selected. Please select a product first by typing its ID.")

def cancel(update, context):
    if "product_id" in context.user_data:
        del context.user_data["product_id"]
        context.bot.send_message(chat_id=update.message.chat_id, text="Purchase cancelled.")
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="No purchase in progress.")

def main():
    # Get the bot's token from the BotFather
    bot_token = "1628769223:AAGii1PYJgngyGWxtT1v71NnISwL5IvRavI"

    # Create an Updater and pass it the bot's token
    updater = Updater(bot_token, use_context=True)

    # Get the dispatcher to

