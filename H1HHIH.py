import telebot
import requests

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('6378129166:AAGJgpDvfHjsd758sDJ42mzfA9LlSi7KsYo')

# Define a function to handle '/start' command
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to EvilGPT bot! Send me a message.')

# Define a function to handle regular messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    user_message = message.text

    if user_message.lower() == 'exit':
        bot.reply_to(message, 'The conversation has ended.')
        return

    url = "https://dev-gpts.pantheonsite.io/wp-admin/js/apis/Se7en_Eyes/EvilGPT.php?text=" + user_message
    response = requests.get(url).text
    bot.reply_to(message, 'EvilGPT: ' + response)

# Polling to get updates
bot.polling()
