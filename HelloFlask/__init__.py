import telebot
import os
from flask import Flask, request
# from main_bot import Respond

TOKEN = '940320468:AAEmAv4SV7b-FdZpuP4NTUSw-AH8uf5eixo'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to('Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@app.route("/{}".format(TOKEN), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://keklol.ru/{}".format(TOKEN))
    return "!", 200
