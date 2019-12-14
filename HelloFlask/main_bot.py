import telebot

bot = telebot.TeleBot('940320468:AAEmAv4SV7b-FdZpuP4NTUSw-AH8uf5eixo')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):

	bot.reply_to(message, message.text)