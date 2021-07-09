from flask import Flask, render_template, request

import json
import string
import random
import nltk
import requests

application = Flask(__name__, template_folder='templates')
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
bot = ChatBot('A.U.R.A')


trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
@application .route("/")
def welcome():
    return render_template("welcome.html")


# define app routes
@application .route("/index/")
def index():
    return render_template("index.html")


@application .route("/about_us/")
def about_us():
    return render_template("about_us.html")


@application .route("/get")
# function for the bot response
def get_bot_response():
        user = request.args.get("msg")

        response = bot.get_response(user)
        return str(response)



if __name__ == "__main__":
    application .run()
