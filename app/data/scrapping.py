import requests
from bs4 import BeautifulSoup
from .model import DayImage, Covid
from ..config import Config
from flask import Blueprint, request, Response
import pandas as pd
from sodapy import Socrata
from unicodedata import normalize


def get_day_image():
    r = requests.get('https://www.minsalud.gov.co/salud/publica/PET/Paginas/Covid-19_copia.aspx')
    soup = BeautifulSoup(r.text, 'html.parser')

    resultsRow = soup.find_all('div', attrs={'id': 'WebPartWPQ4'})

    results = []
    origin_url = 'https://www.minsalud.gov.co'
    for resultRow in resultsRow:
        text = "Imagen del dia"
        img = resultRow.find('img').get('src')
    
        results.append({
            'text': text,
            'img': origin_url + img
        })
    save_data_image(results)


def save_data_image(data: list):    
    DayImage(title=data[0]['text'], url=data[0]['img']).save()


def get_data():
    client = Socrata("www.datos.gov.co", Config.DATOS_GOV_KEY)
    results = client.get("gt2j-8ykr", limit=10000)
    results_df = pd.DataFrame.from_records(results)
    results_df.index = results_df['id_de_caso']
    results_df = results_df.drop('id_de_caso', axis=1)

    f = lambda x : x.astype(str).str.lower()
    translate_lambda = lambda s : s.astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    results_df = results_df.apply(f)
    results_df = results_df.apply(translate_lambda)

    # results_df.to_csv('covid19-colombia.csv')

    Covid.drop_collection()
    with open('covid19-colombia.csv', 'r') as file:
        data = file.readlines()
        for info in data:            
            id_case, date, city, departament, atention, age, sex, tipo, procedence = info.split(',')
            Covid(id_caso=id_case, fecha_diagnostico=date, ciudad_ubicacion=city,
                departamento=departament, atencion=atention, edad=age, sexo=sex, 
                tipo=tipo, pais_procedencia=procedence).save()
