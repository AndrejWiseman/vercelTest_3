import requests
from flask import render_template, url_for
from datetime import datetime, timedelta

def prognoza():

    city = 'Prnjavor'
    api_key = '648f71380344c14f8d30afd84d40cf00'
    api_call1 = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=' + city + '&units=metric&lang=sr'

    json_data1 = requests.get(api_call1).json()

    tr_opis = json_data1['list'][0]['weather'][0]['description']
    tr_vlaznost = json_data1['list'][0]['main']['humidity']

    api_call = 'https://api.open-meteo.com/v1/forecast?latitude=44.87&longitude=17.66&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&windspeed_unit=kmh&timeformat=unixtime&timezone=Europe%2FBerlin'

    json_data = requests.get(api_call).json()

    dani = json_data['daily']['time']
    temp_max = json_data['daily']['temperature_2m_max']
    temp_min = json_data['daily']['temperature_2m_min']
    brz_vetra = json_data['daily']['windspeed_10m_max']
    vrem_kodovi = json_data['daily']['weathercode']
    izlasci = json_data['daily']['sunrise']
    zalasci = json_data['daily']['sunset']

    trenutna_temp = round(json_data['current_weather']['temperature'])
    trenutni_code = json_data['current_weather']['weathercode']

    danas_max = round(temp_max[0])
    danas_min = round(temp_min[0])
    danas_code = vrem_kodovi[0]
    danas_vetar = round(brz_vetra[0])
    danas_izlazak = datetime.fromtimestamp(izlasci[0]) + timedelta(hours=1)
    danas_zalazak = datetime.fromtimestamp(zalasci[0]) + timedelta(hours=1)
    izlazak_sunca = danas_izlazak.strftime(" %H:%M")
    zalazak_sunca = danas_zalazak.strftime(" %H:%M")

    sutra_max = round(temp_max[1])
    sutra_min = round(temp_min[1])
    sutra_code = vrem_kodovi[1]

    prekosutra_max = round(temp_max[2])
    prekosutra_min = round(temp_min[2])
    prekosutra_code = vrem_kodovi[2]

    za_dva_dana_max = round(temp_max[3])
    za_dva_dana_min = round(temp_min[3])
    za_dva_dana_code = vrem_kodovi[3]

    za_tri_dana_max = round(temp_max[4])
    za_tri_dana_min = round(temp_min[4])
    za_tri_dana_code = vrem_kodovi[4]

    danasnja = dani[0], temp_max[0], temp_min[0]
    sutrasnja = dani[1], temp_max[1], temp_min[1]
    prekosutrasnja = dani[2], temp_max[2], temp_min[2]

    timestamp = dani[0]
    str = dani[1]
    prst = dani[2]
    dt_obj = datetime.fromtimestamp(timestamp).strftime('%d.%m.%y')
    str1 = datetime.fromtimestamp(str).strftime('%d.%m.%y')
    prst1 = datetime.fromtimestamp(prst).strftime('%d.%m.%y')
    d = datetime.now()
    da = d.weekday()
    dni = ['Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak', 'Subota', 'Nedelja']
    s1 = d + timedelta(days=1)
    ps1 = d + timedelta(days=2)
    pps1 = d + timedelta(days=3)
    ppps1 = d + timedelta(days=4)
    s11 = s1.weekday()
    ps11 = ps1.weekday()
    pps11 = pps1.weekday()
    ppps11 = ppps1.weekday()
    danas1 = dni[da]
    sutra1 = dni[s11]
    prekosutra1 = dni[ps11]
    dva_dana1 = dni[pps11]
    tri_dana1 = dni[ppps11]

    opis = ''
    if trenutni_code == 0:
        opis = 'Vedro'
    elif trenutni_code == 1:
        opis = 'Delimično vedro'
    elif trenutni_code == 2:
        opis = 'Delimično oblačno'
    elif trenutni_code == 3:
        opis = 'Oblačno'
    elif trenutni_code == 45:
        opis = 'Magla'
    elif trenutni_code == 48:
        opis = 'Ledena izmaglica'
    elif trenutni_code == 51:
        opis = 'Lagana kišica'
    elif trenutni_code == 56:
        opis = 'Ledena kišica'
    elif trenutni_code == 57:
        opis = 'Ledena kišica'
    elif trenutni_code == 61:
        opis = 'Lagana kiša'
    elif trenutni_code == 63:
        opis = 'Kiša'
    elif trenutni_code == 65:
        opis = 'Pljuskovi'
    elif trenutni_code == 66:
        opis = 'Ledena kiša'
    elif trenutni_code == 67:
        opis = 'Ledeni pljusak'
    elif trenutni_code == 71:
        opis = 'Lagani sneg'
    elif trenutni_code == 73:
        opis = 'Sneg'
    elif trenutni_code == 75:
        opis = 'Snezne padavine'
    elif trenutni_code == 77:
        opis = 'Krupni sneg'
    elif trenutni_code == 80:
        opis = 'Lagani pljuskovi'
    elif trenutni_code == 81:
        opis = 'Pljuskovi'
    elif trenutni_code == 82:
        opis = 'Jaki pljuskovi'
    elif trenutni_code == 85:
        opis = 'Jak sneg'
    elif trenutni_code == 86:
        opis = 'Mećava'
    elif trenutni_code == 95:
        opis = 'Grmljavina'
    elif trenutni_code == 96:
        opis = 'Nevreme sa grmljavinom'
    elif trenutni_code == 99:
        opis = 'Nevreme sa grmljavinom'

#---------------------------------------------------
    api_call_air = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=44.87&lon=17.66&appid=648f71380344c14f8d30afd84d40cf00'
    json_data_air = requests.get(api_call_air).json()
    air_index = json_data_air['list'][0]['main']['aqi']

    kvalitet_vazduha = ''
    if air_index == 1:
        kvalitet_vazduha = 'Dobar'
    elif air_index == 2:
        kvalitet_vazduha = 'Zadovoljavajući'
    elif air_index == 3:
        kvalitet_vazduha = 'Osrednji'
    elif air_index == 4:
        kvalitet_vazduha = 'Loš'
    elif air_index == 5:
        kvalitet_vazduha = 'Veoma loš'


# ---- Banja Luka -----------------------
    # ========================
    city2 = 'Banja Luka'
    api_key = '648f71380344c14f8d30afd84d40cf00'
    api_callbl = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=' + city2 + '&units=metric&lang=sr'

    json_databl = requests.get(api_callbl).json()

    tr_vlaznostbl = json_databl['list'][0]['main']['humidity']

    api_callbl = 'https://api.open-meteo.com/v1/forecast?latitude=44.77&longitude=17.18&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&windspeed_unit=ms&timeformat=unixtime&timezone=Europe%2FBerlin'

    json_databl = requests.get(api_callbl).json()

    danibl = json_databl['daily']['time']
    temp_maxbl = json_databl['daily']['temperature_2m_max']
    temp_minbl = json_databl['daily']['temperature_2m_min']
    brz_vetrabl = json_databl['daily']['windspeed_10m_max']
    vrem_kodovibl = json_databl['daily']['weathercode']
    izlascibl = json_databl['daily']['sunrise']
    zalascibl = json_databl['daily']['sunset']

    trenutna_tempbl = round(json_databl['current_weather']['temperature'])
    trenutni_codebl = json_databl['current_weather']['weathercode']

    danas_maxbl = round(temp_maxbl[0])
    danas_minbl = round(temp_minbl[0])
    danas_codebl = vrem_kodovibl[0]
    danas_vetarbl = round(brz_vetrabl[0])
    danas_izlazakbl = datetime.fromtimestamp(izlascibl[0]) + timedelta(hours=1)
    danas_zalazakbl = datetime.fromtimestamp(zalascibl[0]) + timedelta(hours=1)
    izlazak_suncabl = danas_izlazakbl.strftime(" %H:%M")
    zalazak_suncabl = danas_zalazakbl.strftime(" %H:%M")

    sutra_maxbl = round(temp_maxbl[1])
    sutra_minbl = round(temp_minbl[1])
    sutra_codebl = vrem_kodovibl[1]

    prekosutra_maxbl = round(temp_maxbl[2])
    prekosutra_minbl = round(temp_minbl[2])
    prekosutra_codebl = vrem_kodovibl[2]

    za_dva_dana_maxbl = round(temp_maxbl[3])
    za_dva_dana_minbl = round(temp_minbl[3])
    za_dva_dana_codebl = vrem_kodovibl[3]

    za_tri_dana_maxbl = round(temp_maxbl[4])
    za_tri_dana_minbl = round(temp_minbl[4])
    za_tri_dana_codebl = vrem_kodovibl[4]

    timestampbl = danibl[0]
    strbl = danibl[1]
    prstbl = danibl[2]
    dt_objbl = datetime.fromtimestamp(timestampbl).strftime('%d.%m.%y')
    str1bl = datetime.fromtimestamp(strbl).strftime('%d.%m.%y')
    prst1bl = datetime.fromtimestamp(prstbl).strftime('%d.%m.%y')
    dbl = datetime.now()
    dabl = dbl.weekday()
    dnibl = ['Ponedeljak', 'Utorak', 'Sreda', 'Četvrtak', 'Petak', 'Subota', 'Nedelja']
    s1bl = dbl + timedelta(days=1)
    ps1bl = dbl + timedelta(days=2)
    pps1bl = dbl + timedelta(days=3)
    ppps1bl = dbl + timedelta(days=4)
    s11bl = s1bl.weekday()
    ps11bl = ps1bl.weekday()
    pps11bl = pps1bl.weekday()
    ppps11bl = ppps1bl.weekday()
    danas1bl = dnibl[dabl]
    sutra1bl = dnibl[s11bl]
    prekosutra1bl = dnibl[ps11bl]
    dva_dana1bl = dnibl[pps11bl]
    tri_dana1bl = dnibl[ppps11bl]

    opisbl = ''
    if trenutni_codebl == 0:
        opisbl = 'Vedro'
    elif trenutni_codebl == 1:
        opisbl = 'Delimično vedro'
    elif trenutni_codebl == 2:
        opisbl = 'Delimično oblačno'
    elif trenutni_codebl == 3:
        opisbl = 'Oblačno'
    elif trenutni_codebl == 45:
        opisbl = 'Magla'
    elif trenutni_codebl == 48:
        opisbl = 'Ledena izmaglica'
    elif trenutni_codebl == 51:
        opisbl = 'Lagana kišica'
    elif trenutni_codebl == 56:
        opisbl = 'Ledena kišica'
    elif trenutni_codebl == 57:
        opisbl = 'Ledena kišica'
    elif trenutni_codebl == 61:
        opisbl = 'Lagana kiša'
    elif trenutni_codebl == 63:
        opisbl = 'Kiša'
    elif trenutni_codebl == 65:
        opisbl = 'Pljuskovi'
    elif trenutni_codebl == 66:
        opisbl = 'Ledena kiša'
    elif trenutni_codebl == 67:
        opisbl = 'Ledeni pljusak'
    elif trenutni_codebl == 71:
        opisbl = 'Lagani sneg'
    elif trenutni_codebl == 73:
        opisbl = 'Sneg'
    elif trenutni_codebl == 75:
        opisbl = 'Snezne padavine'
    elif trenutni_codebl == 77:
        opisbl = 'Krupni sneg'
    elif trenutni_codebl == 80:
        opisbl = 'Lagani pljuskovi'
    elif trenutni_codebl == 81:
        opisbl = 'Pljuskovi'
    elif trenutni_codebl == 82:
        opisbl = 'Jaki pljuskovi'
    elif trenutni_codebl == 85:
        opisbl = 'Jak sneg'
    elif trenutni_codebl == 86:
        opisbl = 'Mećava'
    elif trenutni_codebl == 95:
        opisbl = 'Grmljavina'
    elif trenutni_codebl == 96:
        opisbl = 'Nevreme sa grmljavinom'
    elif trenutni_codebl == 99:
        opisbl = 'Nevreme sa grmljavinom'

    # ---------------------------------------------------
    api_call_airbl = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=44.77&lon=17.19&appid=648f71380344c14f8d30afd84d40cf00'
    json_data_airbl = requests.get(api_call_airbl).json()
    air_indexbl = json_data_airbl['list'][0]['main']['aqi']

    kvalitet_vazduhabl = ''
    if air_indexbl == 1:
        kvalitet_vazduhabl = 'Dobar'
    elif air_indexbl == 2:
        kvalitet_vazduhabl = 'Zadovoljavajući'
    elif air_indexbl == 3:
        kvalitet_vazduhabl = 'Osrednji'
    elif air_indexbl == 4:
        kvalitet_vazduhabl = 'Loš'
    elif air_indexbl == 5:
        kvalitet_vazduhabl = 'Veoma loš'




# ------ Sent Galen ---------------
    # ========================
    city3 = 'Sankt Gallen'
    api_key = '648f71380344c14f8d30afd84d40cf00'
    api_callsg = 'https://api.openweathermap.org/data/2.5/forecast?appid=' + api_key + '&q=' + city2 + '&units=metric&lang=sr'

    json_datasg = requests.get(api_callsg).json()

    tr_vlaznostsg = json_datasg['list'][0]['main']['humidity']

    api_callsg = 'https://api.open-meteo.com/v1/forecast?latitude=47.42&longitude=9.37&daily=weathercode,temperature_2m_max,temperature_2m_min,sunrise,sunset,windspeed_10m_max&current_weather=true&windspeed_unit=kmh&timeformat=unixtime&timezone=Europe%2FBerlin'

    json_datasg = requests.get(api_callsg).json()

    danisg = json_datasg['daily']['time']
    temp_maxsg = json_datasg['daily']['temperature_2m_max']
    temp_minsg = json_datasg['daily']['temperature_2m_min']
    brz_vetrasg = json_datasg['daily']['windspeed_10m_max']
    vrem_kodovisg = json_datasg['daily']['weathercode']
    izlascisg = json_datasg['daily']['sunrise']
    zalascisg = json_datasg['daily']['sunset']

    trenutna_tempsg = round(json_datasg['current_weather']['temperature'])
    trenutni_codesg = json_datasg['current_weather']['weathercode']

    danas_maxsg = round(temp_maxsg[0])
    danas_minsg = round(temp_minsg[0])
    danas_codesg = vrem_kodovisg[0]
    danas_vetarsg = round(brz_vetrasg[0])
    danas_izlazaksg = datetime.fromtimestamp(izlascisg[0]) + timedelta(hours=1)
    danas_zalazaksg = datetime.fromtimestamp(zalascisg[0]) + timedelta(hours=1)
    izlazak_suncasg = danas_izlazaksg.strftime(" %H:%M")
    zalazak_suncasg = danas_zalazaksg.strftime(" %H:%M")

    sutra_maxsg = round(temp_maxsg[1])
    sutra_minsg = round(temp_minsg[1])
    sutra_codesg = vrem_kodovisg[1]

    prekosutra_maxsg = round(temp_maxsg[2])
    prekosutra_minsg = round(temp_minsg[2])
    prekosutra_codesg = vrem_kodovisg[2]

    za_dva_dana_maxsg = round(temp_maxsg[3])
    za_dva_dana_minsg = round(temp_minsg[3])
    za_dva_dana_codesg = vrem_kodovisg[3]

    za_tri_dana_maxsg = round(temp_maxsg[4])
    za_tri_dana_minsg = round(temp_minsg[4])
    za_tri_dana_codesg = vrem_kodovisg[4]


    opissg = ''
    if trenutni_codesg == 0:
        opissg = 'Vedro'
    elif trenutni_codesg == 1:
        opissg = 'Delimično vedro'
    elif trenutni_codesg == 2:
        opissg = 'Delimično oblačno'
    elif trenutni_codesg == 3:
        opissg = 'Oblačno'
    elif trenutni_codesg == 45:
        opissg = 'Magla'
    elif trenutni_codesg == 48:
        opissg = 'Ledena izmaglica'
    elif trenutni_codesg == 51:
        opissg = 'Lagana kišica'
    elif trenutni_codesg == 56:
        opissg = 'Ledena kišica'
    elif trenutni_codesg == 57:
        opissg = 'Ledena kišica'
    elif trenutni_codesg == 61:
        opissg = 'Lagana kiša'
    elif trenutni_codesg == 63:
        opissg = 'Kiša'
    elif trenutni_codesg == 65:
        opissg = 'Pljuskovi'
    elif trenutni_codesg == 66:
        opissg = 'Ledena kiša'
    elif trenutni_codesg == 67:
        opissg = 'Ledeni pljusak'
    elif trenutni_codesg == 71:
        opissg = 'Lagani sneg'
    elif trenutni_codesg == 73:
        opissg = 'Sneg'
    elif trenutni_codesg == 75:
        opissg = 'Snezne padavine'
    elif trenutni_codesg == 77:
        opissg = 'Krupni sneg'
    elif trenutni_codesg == 80:
        opissg = 'Lagani pljuskovi'
    elif trenutni_code == 81:
        opissg = 'Pljuskovi'
    elif trenutni_codesg == 82:
        opissg = 'Jaki pljuskovi'
    elif trenutni_codesg == 85:
        opissg = 'Jak sneg'
    elif trenutni_codesg == 86:
        opissg = 'Mećava'
    elif trenutni_code == 95:
        opis = 'Grmljavina'
    elif trenutni_codesg == 96:
        opissg = 'Nevreme sa grmljavinom'
    elif trenutni_codesg == 99:
        opissg = 'Nevreme sa grmljavinom'

    # ---------------------------------------------------
    api_call_airsg = 'http://api.openweathermap.org/data/2.5/air_pollution?lat=47.42&lon=9.37&appid=648f71380344c14f8d30afd84d40cf00'
    json_data_airsg = requests.get(api_call_airsg).json()
    air_indexsg = json_data_airsg['list'][0]['main']['aqi']

    kvalitet_vazduhasg = ''
    if air_indexsg == 1:
        kvalitet_vazduhasg = 'Dobar'
    elif air_indexsg == 2:
        kvalitet_vazduhasg = 'Zadovoljavajući'
    elif air_indexsg == 3:
        kvalitet_vazduhasg = 'Osrednji'
    elif air_indexsg == 4:
        kvalitet_vazduhasg = 'Loš'
    elif air_indexsg == 5:
        kvalitet_vazduhasg = 'Veoma loš'









    return render_template('vreme.html', trenutna_temp=trenutna_temp, sutra1=sutra1, prekosutra1=prekosutra1, sutra_max=sutra_max, sutra_min=sutra_min, prekosutra_max=prekosutra_max, prekosutra_min=prekosutra_min, danas_vetar=danas_vetar, dva_dana1=dva_dana1, za_dva_dana_max=za_dva_dana_max, za_dva_dana_min=za_dva_dana_min, tri_dana1=tri_dana1,  za_tri_dana_max=za_tri_dana_max, za_tri_dana_min=za_tri_dana_min, trenutni_code=trenutni_code, tr_opis=tr_opis,  tr_vlaznost=tr_vlaznost, opis=opis,  za_tri_dana_code=za_tri_dana_code, sutra_code=sutra_code, prekosutra_code=prekosutra_code, za_dva_dana_code=za_dva_dana_code, zalazak_sunca=zalazak_sunca, izlazak_sunca=izlazak_sunca, kvalitet_vazduha=kvalitet_vazduha, air_index=air_index, trenutna_tempbl=trenutna_tempbl, sutra1bl=sutra1bl, prekosutra1bl=prekosutra1bl, sutra_maxbl=sutra_maxbl, sutra_minbl=sutra_minbl, prekosutra_maxbl=prekosutra_maxbl, prekosutra_minbl=prekosutra_minbl, danas_vetarbl=danas_vetarbl, dva_dana1bl=dva_dana1bl, za_dva_dana_maxbl=za_dva_dana_maxbl, za_dva_dana_minbl=za_dva_dana_minbl, tri_dana1bl=tri_dana1bl,  za_tri_dana_maxbl=za_tri_dana_maxbl, za_tri_dana_minbl=za_tri_dana_minbl, trenutni_codebl=trenutni_codebl,  tr_vlaznostbl=tr_vlaznostbl, opisbl=opisbl, za_tri_dana_codebl=za_tri_dana_codebl, sutra_codebl=sutra_codebl, prekosutra_codebl=prekosutra_codebl, za_dva_dana_codebl=za_dva_dana_codebl, zalazak_suncabl=zalazak_suncabl, izlazak_suncabl=izlazak_suncabl, kvalitet_vazduhabl=kvalitet_vazduhabl, air_indexbl=air_indexbl,       trenutna_tempsg=trenutna_tempsg,  sutra_maxsg=sutra_maxsg, sutra_minsg=sutra_minsg, prekosutra_maxsg=prekosutra_maxsg, prekosutra_minsg=prekosutra_minsg, danas_vetarsg=danas_vetarsg,  za_dva_dana_maxsg=za_dva_dana_maxsg, za_dva_dana_minsg=za_dva_dana_minsg,   za_tri_dana_maxsg=za_tri_dana_maxsg, za_tri_dana_minsg=za_tri_dana_minsg, trenutni_codesg=trenutni_codesg, tr_vlaznostsg=tr_vlaznostsg, opissg=opissg,  za_tri_dana_codesg=za_tri_dana_codesg, sutra_codesg=sutra_codesg, prekosutra_codesg=prekosutra_codesg, za_dva_dana_codesg=za_dva_dana_codesg, zalazak_suncasg=zalazak_suncasg, izlazak_suncasg=izlazak_suncasg, kvalitet_vazduhasg=kvalitet_vazduhasg, air_indexsg=air_indexsg   )




# tri_dana1sg=tri_dana1sg,sutra1sg=sutra1sg, prekosutra1sg=prekosutra1sg,dva_dana1sg=dva_dana1sg,