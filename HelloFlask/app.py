import telebot
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from key_word import KeyWord

dir_path = os.getcwd()

TOKEN = '940320468:AAEmAv4SV7b-FdZpuP4NTUSw-AH8uf5eixo'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+dir_path+'/bot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to('Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):

    text = KeyWord(message)
    bot.reply_to(message, text)

@app.route("/{}".format(TOKEN), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://keklol.ru/{}".format(TOKEN))
    return "!", 200
