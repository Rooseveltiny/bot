from flask import Flask, request
from key_word import KeyWord
import telebot
import os
from models import db
from tests import perform_tests


dir_path = os.getcwd()

TOKEN = '940320468:AAEmAv4SV7b-FdZpuP4NTUSw-AH8uf5eixo'
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+dir_path+'/bot.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to('Hello, ' + message.from_user.first_name)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):

    text = KeyWord(message).result
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

@app.route("/tests")
def webhook_tests():
    
    try:
        text = perform_tests()
    except Exception as err:
        text = str(err)

    return text, 200

if __name__ == '__main__':
    app.run(use_debugger=False, use_reloader=False, passthrough_errors=True)


