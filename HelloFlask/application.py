from flask import Flask, request
from key_word import KeyWord
import telebot
import os
from flask_sqlalchemy import SQLAlchemy

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

    # text = KeyWord(message)
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
    
    perform_tests()
    return "!", 200


'''
Some models are presented here!
'''
class CurrentWebSite(db.Model):

    user = db.Column(db.Integer, primary_key = True)
    current_web_site = db.Column(db.String(50))

    def __repl__(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def str(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def users_web_site(self, type_string=False):

        if type_string:
            return self.query.filter_by(user = self.user).first().current_web_site
        return self.query.filter_by(user = self.user)

    def save(self):

        current_web_site = self.users_web_site()
        if current_web_site:
            current_web_site.update({'current_web_site': self.current_web_site})
            db.session.commit()
        else:
            db.session.add(self)
            db.session.commit()

