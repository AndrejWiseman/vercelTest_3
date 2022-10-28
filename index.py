from flask import Flask, render_template, url_for
import requests
import time
from vreme import prognoza

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/vreme')
def vreme():
    # return prognoza()
    api_key = '648f71380344c14f8d30afd84d40cf00'

    grad = 'Prnjavor'


    url = f'https://api.openweathermap.org/data/2.5/weather?q={grad}&appid={api_key}&units=metric&lang=sr'

    response = requests.get(url).json()

    temp = round(response['main']['temp'])
    feels_like = round(response['main']['feels_like'])
    vlaznost = response['main']['humidity']
    vetar = round(response['wind']['speed'])
    icon = response['weather'][0]['icon']

    opis = response['weather'][0]['description']
    sunrise_time = time.localtime(response['sys']['sunrise'])
    sunset_time = time.localtime(response['sys']['sunset'])

    izlazak_sunca = time.strftime("%H:%M", sunrise_time)
    zalazak_sunca = time.strftime("%H:%M", sunset_time)

    return render_template('vreme.html', temp=temp, feels_like=feels_like, vlaznost=vlaznost, vetar=vetar, icon=icon,
                           opis=opis, izlazak_sunca=izlazak_sunca, zalazak_sunca=zalazak_sunca)


if __name__ == '__main__':
    app.run(debug=True)
