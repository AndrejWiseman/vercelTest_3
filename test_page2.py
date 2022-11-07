import requests
from flask import render_template
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import re
import random



# # def prognoza():
# api_call = 'https://api.open-meteo.com/v1/forecast?latitude=44.87&longitude=17.66&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&windspeed_unit=kmh&timeformat=unixtime&timezone=Europe%2FBerlin'
#
# json_data = requests.get(api_call).json()
#
# dani = json_data['daily']['time']
# temp_max = json_data['daily']['temperature_2m_max']
# temp_min = json_data['daily']['temperature_2m_min']
# brz_vetra = json_data['daily']['windspeed_10m_max']
# vrem_kodovi = json_data['daily']['weathercode']
# izlasci = json_data['daily']['sunrise']
# zalasci = json_data['daily']['sunset']
#
# trenutna_temp = round(json_data['current_weather']['temperature'])
# trenutni_code = json_data['current_weather']['weathercode']
#
# danas_max = round(temp_max[0])
# danas_min = round(temp_min[0])
# danas_code = vrem_kodovi[0]
# danas_vetar = round(brz_vetra[0])
# danas_izlazak = datetime.fromtimestamp(izlasci[0])
# danas_zalazak = datetime.fromtimestamp(zalasci[0])
# izlazak_sunca = danas_izlazak.strftime(" %H:%M")
# zalazak_sunca = danas_zalazak.strftime(" %H:%M")
#
# print(izlazak_sunca)
#
# sutra_max = round(temp_max[1])
# sutra_min = round(temp_min[1])
# sutra_code = vrem_kodovi[1]
#
# prekosutra_max = round(temp_max[2])
# prekosutra_min = round(temp_min[2])
# prekosutra_code = vrem_kodovi[2]
#
# za_dva_dana_max = round(temp_max[3])
# za_dva_dana_min = round(temp_min[3])
# za_dva_dana_code = vrem_kodovi[3]
#
# za_tri_dana_max = round(temp_max[4])
# za_tri_dana_min = round(temp_min[4])
# za_tri_dana_code = vrem_kodovi[4]
#
#
# print()
#
#
#
# danasnja = dani[0],temp_max[0],temp_min[0]
# sutrasnja = dani[1],temp_max[1],temp_min[1]
# prekosutrasnja = dani[2],temp_max[2],temp_min[2]
#
#
#
# timestamp = dani[0]
# str = dani[1]
# prst = dani[2]
# dt_obj = datetime.fromtimestamp(timestamp).strftime('%d.%m.%y')
# str1 = datetime.fromtimestamp(str).strftime('%d.%m.%y')
# prst1 = datetime.fromtimestamp(prst).strftime('%d.%m.%y')
#
#
#
# # d = datetime.now()
# # da = d.weekday()
# #
# # dni = ['Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak', 'Subota', 'Nedelja']
# #
# # danas1 = dni[da]
# # sutra1 = dni[da + 1]
# # prekosutra1 = dni[da + 2]
# # dva_dana1 = dni[da + 3]
# # # tri_dana1 = dni[da + 4]
#
# # print('Danas je', dt_obj, 'to jest', danas1)
# # print('Sutra je', str1, 'to jest', sutra1)
# # print('Prekosutra je', prst1, 'to jest', prekosutra1)
# #
# # # print(trenutno)
# # # print('Trenutno je, ',round(trenutno), '°C', 'brzina vetra je ', round(json_data['current_weather']['windspeed']),'km/h' )
# # print('Danas, ', dani[0], ' ce bit maksimalna temperatura ', temp_max[0], ', a minimalna ', temp_min[0], 'C' )
# # print('Sutra, ', dani[1], ' ce bit maksimalna temperatura ', temp_max[1], ', a minimalna ', temp_min[1], 'C' )
# # print('Prekosutra, ', dani[2], ' ce bit maksimalna temperatura ', temp_max[2], ', a minimalna ', temp_min[2], 'C' )
# #
# #
# # print(dani)
# # # print(json_data['current_weather']['temperature'])
# # print(json_data)
#
# #---------------------------------------------
# opis = ''
# icon_code = ''
#
# # for code in vrem_kodovi:
#
# if vrem_kodovi == 0:
#     opis = 'Vedro'
#     icon_code = '01d'
# # elif code == 1:
# #     opis = 'Delimično vedro'
# #     icon_code = '02d'
# # elif code == 2:
# #     opis = 'Delimično oblačno'
# #     icon_code = '03d'
# # elif code == 3:
# #     opis = 'Oblačno'
# #     icon_code = '04d'
# elif vrem_kodovi == 45:
#     opis = 'Magla'
#     icon_code = ('50d')
# # elif code == 48:
# #     opis = 'Ledena izmaglica'
# #     icon_code = '50d'
# # elif code == 51:
# #     opis = 'Lagana kišica'
# #     icon_code = '09d'
#
#
# #-----------------------------------------------------
#
#
# # api_call_air = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=44.87&lon=17.66&appid=648f71380344c14f8d30afd84d40cf00'
# # json_data_air = requests.get(api_call_air).json()
# # air_index = json_data_air['list'][0]['main']['aqi']
# #
# # kvalitet_vazduha = ''
# # if air_index == 1:
# #     kvalitet_vazduha = 'Dobar'
# # elif air_index == 2:
# #     kvalitet_vazduha = 'Zadovoljavajući'
# # elif air_index == 3:
# #     kvalitet_vazduha = 'Osrednji'
# # elif air_index == 4:
# #     kvalitet_vazduha = 'Loš'
# # elif air_index == 5:
# #     kvalitet_vazduha = 'Veoma loš'
# #
# # print(air_index)
#
#
#
#
#
#
# air_call = 'https://air-quality-api.open-meteo.com/v1/air-quality?latitude=44.87&longitude=17.66&hourly=pm10,pm2_5,nitrogen_dioxide,ragweed_pollen&domains=cams_europe&timezone=Europe%2FBerlin'
#
# air_json = requests.get(air_call).json()
#
# pm10 = air_json['hourly']['pm10'][:24]
# pm25 = air_json['hourly']['pm2_5'][:24]
# ndox = air_json['hourly']['nitrogen_dioxide'][:24]
# ambrozija = air_json['hourly']['ragweed_pollen'][:24]
#
# pm10_uk = 0
# for pm1 in pm10:
#     pm10_uk += pm1
# pm10_prosek = round(pm10_uk / len(pm10))
#
# pm25_uk = 0
# for pm2 in pm25:
#     pm25_uk += pm2
# pm25_prosek = round(pm25_uk / len(pm25))
#
# nd2 = 0
# for nd in ndox:
#     nd2 += nd
# nd_prosek = round(nd2 / len(ndox))
#
# # amb = 0
# # for am in ambrozija:
# #     amb += am
# # amb_prosek = round(amb / len(ambrozija))
#
# zagadjenje = ''
# if 0 < pm10_prosek < 25 and 0 < pm25_prosek < 15 and 0 < nd_prosek < 50:
#     zagadjenje = 'Dobar'
# elif 25 <= pm10_prosek < 50 or 15 <= pm25_prosek < 30 or 50 <= nd_prosek < 100:
#     zagadjenje = 'Zadovoljavajući'
# elif 50 <= pm10_prosek < 90 or 30 <= pm25_prosek < 55 or 100 <= nd_prosek < 200:
#     zagadjenje = 'Osrednji'
# elif 90 <= pm10_prosek < 180 or 55 <= pm25_prosek < 110 or 200 <= nd_prosek < 400:
#     zagadjenje = 'Loš'
# elif pm10_prosek >= 180 or pm25_prosek >= 110 or nd_prosek >= 400:
#     zagadjenje = 'Veoma loš'
# else:
#     zagadjenje = 'Ne mogu da ucitam'
#
#
#
# # ========================
# city2 = 'Banja Luka'
# api_key = '648f71380344c14f8d30afd84d40cf00'
# api_callbl = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=' + city2 + '&units=metric&lang=sr'
#
# json_databl = requests.get(api_callbl).json()
#
# tr_vlaznostbl = json_databl['list'][0]['main']['humidity']
#
#
# api_callbl = 'https://api.open-meteo.com/v1/forecast?latitude=44.77&longitude=17.19&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&windspeed_unit=ms&timeformat=unixtime&timezone=Europe%2FBerlin'
#
# json_databl = requests.get(api_callbl).json()
#
# danibl = json_databl['daily']['time']
# temp_maxbl = json_databl['daily']['temperature_2m_max']
# temp_minbl = json_databl['daily']['temperature_2m_min']
# brz_vetrabl = json_databl['daily']['windspeed_10m_max']
# vrem_kodovibl = json_databl['daily']['weathercode']
# izlascibl = json_databl['daily']['sunrise']
# zalascibl = json_databl['daily']['sunset']
#
# trenutna_tempbl = round(json_databl['current_weather']['temperature'])
# trenutni_codebl = json_databl['current_weather']['weathercode']
#
# danas_maxbl = round(temp_maxbl[0])
# danas_minbl = round(temp_minbl[0])
# danas_codebl = vrem_kodovibl[0]
# danas_vetarbl = round(brz_vetrabl[0])
# danas_izlazakbl = datetime.fromtimestamp(izlascibl[0])
# danas_zalazakbl = datetime.fromtimestamp(zalascibl[0])
# izlazak_suncabl = danas_izlazakbl.strftime(" %H:%M")
# zalazak_suncabl = danas_zalazakbl.strftime(" %H:%M")
#
# sutra_maxbl = round(temp_maxbl[1])
# sutra_minbl = round(temp_minbl[1])
# sutra_codebl = vrem_kodovibl[1]
#
# prekosutra_maxbl = round(temp_maxbl[2])
# prekosutra_minbl = round(temp_minbl[2])
# prekosutra_codebl = vrem_kodovibl[2]
#
# za_dva_dana_maxbl = round(temp_maxbl[3])
# za_dva_dana_minbl = round(temp_minbl[3])
# za_dva_dana_codebl = vrem_kodovibl[3]
#
# za_tri_dana_maxbl = round(temp_maxbl[4])
# za_tri_dana_minbl = round(temp_minbl[4])
# za_tri_dana_codebl = vrem_kodovibl[4]
#
# timestampbl = danibl[0]
# strbl = danibl[1]
# prstbl = danibl[2]
# dt_objbl = datetime.fromtimestamp(timestampbl).strftime('%d.%m.%y')
# str1bl = datetime.fromtimestamp(strbl).strftime('%d.%m.%y')
# prst1bl = datetime.fromtimestamp(prstbl).strftime('%d.%m.%y')
# dbl = datetime.now()
# dabl = dbl.weekday()
# dnibl = ['Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak', 'Subota', 'Nedelja']
# s1bl = dbl + timedelta(days=1)
# ps1bl = dbl + timedelta(days=2)
# pps1bl = dbl + timedelta(days=3)
# ppps1bl = dbl + timedelta(days=4)
# s11bl = s1bl.weekday()
# ps11bl = ps1bl.weekday()
# pps11bl = pps1bl.weekday()
# ppps11bl = ppps1bl.weekday()
# danas1bl = dnibl[dabl]
# sutra1bl = dnibl[s11bl]
# prekosutra1bl = dnibl[ps11bl]
# dva_dana1bl = dnibl[pps11bl]
# tri_dana1bl = dnibl[ppps11bl]
#
# opisbl = ''
# if trenutni_codebl == 0:
#     opisbl = 'Vedro'
# elif trenutni_codebl == 1:
#     opisbl = 'Delimično vedro'
# elif trenutni_codebl == 2:
#     opisbl = 'Delimično oblačno'
# elif trenutni_codebl == 3:
#     opisbl = 'Oblačno'
# elif trenutni_codebl == 45:
#     opisbl = 'Magla'
# elif trenutni_codebl == 48:
#     opisbl = 'Ledena izmaglica'
# elif trenutni_codebl == 51:
#     opisbl = 'Lagana kišica'
# elif trenutni_codebl == 56:
#     opisbl = 'Ledena kišica'
# elif trenutni_codebl == 57:
#     opisbl = 'Ledena kišica'
# elif trenutni_codebl == 61:
#     opisbl = 'Lagana kiša'
# elif trenutni_codebl == 63:
#     opisbl = 'Kiša'
# elif trenutni_codebl == 65:
#     opisbl = 'Pljuskovi'
# elif trenutni_codebl == 66:
#     opisbl = 'Ledena kiša'
# elif trenutni_codebl == 67:
#     opisbl = 'Ledeni pljusak'
# elif trenutni_codebl == 71:
#     opisbl = 'Lagani sneg'
# elif trenutni_codebl == 73:
#     opisbl = 'Sneg'
# elif trenutni_codebl == 75:
#     opisbl = 'Snezne padavine'
# elif trenutni_codebl == 77:
#     opisbl = 'Krupni sneg'
# elif trenutni_codebl == 80:
#     opisbl = 'Lagani pljuskovi'
# elif trenutni_codebl == 81:
#     opisbl = 'Pljuskovi'
# elif trenutni_codebl == 82:
#     opisbl = 'Jaki pljuskovi'
# elif trenutni_codebl == 85:
#     opisbl = 'Jak sneg'
# elif trenutni_codebl == 86:
#     opisbl = 'Mećava'
# elif trenutni_codebl == 95:
#     opisbl = 'Grmljavina'
# elif trenutni_codebl == 96:
#     opisbl = 'Nevreme sa grmljavinom'
# elif trenutni_codebl == 99:
#     opisbl = 'Nevreme sa grmljavinom'
#
# #---------------------------------------------------
# api_call_airbl = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=44.77&lon=17.19&appid=648f71380344c14f8d30afd84d40cf00'
# json_data_airbl = requests.get(api_call_airbl).json()
# air_indexbl = json_data_airbl['list'][0]['main']['aqi']
#
# kvalitet_vazduhabl = ''
# if air_indexbl == 1:
#     kvalitet_vazduhabl = 'Dobar'
# elif air_indexbl == 2:
#     kvalitet_vazduhabl = 'Zadovoljavajući'
# elif air_indexbl == 3:
#     kvalitet_vazduhabl = 'Osrednji'
# elif air_indexbl == 4:
#     kvalitet_vazduhabl = 'Loš'
# elif air_indexbl == 5:
#     kvalitet_vazduhabl = 'Veoma loš'
#
# print(kvalitet_vazduhabl)
# ===============================================================
# ===============================================================


# =======================================================
# ---- vicevi -------------------------------------------
#
# url = 'https://www.vicevi.rs/vicevi/grafiti'
#
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')
#
# baza_viceva = []
#
# # vicevi = soup.find_all('div', class_="content")
# vicevi2 = soup.find_all('div', class_="text")
#
# for vic in vicevi2:
#     v = vic.find('p').text
#     baza_viceva.append(v)
#
# # stranice = soup.find('div', class_="pagination-container")
# # br_str = stranice.find_all('li')
#
# # for st in br_str:
# #     s = st.find('a').text
# #     print(s)
#
#
# print(baza_viceva)


#---- Drugi nacin ------------
# s = HTMLSession()
# url = 'https://www.vicevi.rs/vicevi/grafiti'
#
# def getdata(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.content, 'html.parser')
#     return soup
#
# def getnextpage(soup):
#     page = soup.find('ul', class_='pagination')
#     if not page.find('li', class_='disabled')
#         url = 'https://www.vicevi.rs/vicevi/grafiti/' + str(page.find('li'.{'class':'disabled'})).find('a')


#---- treci nacin --------------

baza_viceva = []

# for x in range(1, 35):
#     url = 'https://www.vicevi.rs/vicevi/grafiti/'
#
#     page = requests.get(url + str(x))
#     # soup = BeautifulSoup(page.content, 'html.parser')
#
#     # # vicevi = soup.find_all('div', class_="content")
#     # vicevi2 = soup.find_all('div', class_="text")
#     #
#     # for vic in vicevi2:
#     #     v = vic.find('p')
#     #     baza_viceva.append(v)
#
#
# print(url)

for x in range(1,41):
    url = 'https://www.vicevi.rs/vicevi/crni-humor/'
    page = requests.get(url + str(x))
    soup = BeautifulSoup(page.text, 'html.parser')
    vicevi2 = soup.find_all('div', class_="text")
    for vic in vicevi2:
        v = vic.find('p').text
        baza_viceva.append(v)


print(baza_viceva)



# print(random.choice(baza2))





