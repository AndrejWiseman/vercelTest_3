import requests
from flask import render_template
from datetime import datetime, timedelta

# def prognoza():
global date
city = 'Prnjavor'

api_key = '648f71380344c14f8d30afd84d40cf00'
api_call1 = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=' + city + '&units=metric&lang=sr'

json_data1 = requests.get(api_call1).json()



# for item in json_data['list']:
#     time = item['dt_txt']
#     temp = round(item['main']['temp'])
#
#     # Split the time into date and hour [2018-04-15 06:00:00]
#     next_date, hour = time.split(' ')
#
#     # # Stores the current date and prints it once
#     if current_date != next_date:
#         current_date = next_date
#         year, month, day = current_date.split('-')
#         date = {'y': year, 'm': month, 'd': day}
#         # vreme = '\n{d}.{m}.{y}'.format(**date)
#         datumi = '{d}.{m}.'.format(**date)
#
#         trenutna_vremena.append(datumi)
#
#         # print(datumi)
#
#     sve_temperature.append(temp)
#
#     # Grabs the first 2 integers from our HH:MM:SS string to get the hours
#     hour = int(hour[:2])
#
#     # Sets the AM (ante meridiem) or PM (post meridiem) period
#     if hour < 12:
#         if hour == 0:
#             hour = 12
#         meridiem = 'AM'
#     else:
#         if hour > 12:
#             hour -= 12
#         meridiem = 'PM'

    # Prints the hours [HH:MM AM/PM]
    # print('\n%i:00 %s' % (hour, meridiem))

    # Temperature is measured in Kelvin
    # temperature = round(item['main']['temp'])

    # Weather condition
    # description = item['weather'][0]['description']

    # print('Temperatura je: ', temperature)
    # print('Prognoza je: ', description)

trenutna_temp = round(json_data1['list'][0]['main']['temp'])
tr_icon = json_data1['list'][0]['weather'][0]['icon']
tr_opis = json_data1['list'][0]['weather'][0]['description']
tr_vlaznost = json_data1['list'][0]['main']['humidity']
tr_vetar = round(json_data1['list'][0]['wind']['speed'])




sutra_icon = json_data1['list'][7]['weather'][0]['icon']
sutra_opis = json_data1['list'][7]['weather'][0]['description']
sutra_vlaznost = json_data1['list'][7]['main']['humidity']



prs_icon = json_data1['list'][15]['weather'][0]['icon']
prs_opis = json_data1['list'][15]['weather'][0]['description']
prs_vlaznost = json_data1['list'][15]['main']['humidity']



dva_d_icon = json_data1['list'][23]['weather'][0]['icon']
dva_d_opis = json_data1['list'][23]['weather'][0]['description']
dva_d_vlaznost = json_data1['list'][23]['main']['humidity']


# danas = trenutna_vremena[0]
# sutra = trenutna_vremena[1]
# prekosutra = trenutna_vremena[2]
# dva_d = trenutna_vremena[3]


print(json_data1)

