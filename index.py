from flask import Flask, render_template, url_for
import requests
import time
from vreme import prognoza
from vicevi import vic_random

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/vreme')
def vreme():
    return prognoza()

# @app.route('/vicevi')
# def vic():
#     return vic_random()


if __name__ == '__main__':
    app.run(debug=True)
