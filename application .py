from flask import Flask, render_template, request

import json
import string
import random
import nltk
import requests

app = Flask(__name__, template_folder='templates')
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
bot = ChatBot('A.U.R.A')


trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')
@app.route("/")
def welcome():
    return render_template("welcome.html")





if __name__ == "__main__":
    app.run()
