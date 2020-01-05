import telebot
import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# from key_word import KeyWord

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
    bot.reply_to(message, message.text + '\n' +data)

@app.route("/{}".format(TOKEN), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://keklol.ru/{}".format(TOKEN))
    return "!", 200




### here are models
class CurrentWebSite(db.Model):

    user = db.Column(db.Integer, primary_key = True)
    current_web_site = db.Column(db.String(50))

    def __repl__(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def str(self):

        return 'user is {}, and the current web site is {}'.format(self.user, self.current_web_site)

    def save(self):

        current_web_site = db.session.query(CurrentWebSite).filter_by(user=self.user).first()
        if current_web_site:
            current_web_site.current_web_site = 'lolkek.com'
            db.session.commit()
        else:
            db.session.add(self)
            db.session.commit()

if __name__ == "__main__":
    
    db.create_all()