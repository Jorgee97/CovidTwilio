import requests
from bs4 import BeautifulSoup
from .model import DayImage, Covid, Movies
from ..config import Config
import pandas as pd
from sodapy import Socrata


def get_day_image():
    r = requests.get('https://www.minsalud.gov.co/salud/publica/PET/Paginas/Covid-19_copia.aspx')
    soup = BeautifulSoup(r.text, 'html.parser')

    results_row = soup.find_all('div', attrs={'id': 'WebPartWPQ4'})

    results = []
    origin_url = 'https://www.minsalud.gov.co'
    for resultRow in results_row:
        text = "Casos de COVID19 en Colombia"
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

    f = lambda x: x.astype(str).str.lower()
    translate_lambda = lambda s: s.astype(str).str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode(
        'utf-8')

    results_df = results_df.apply(f)
    results_df = results_df.apply(translate_lambda)

    results_df.to_csv('covid19-colombia.csv')

    Covid.drop_collection()


def save_covid_data():
    with open('covid19-colombia.csv', 'r') as file:
        data = file.readlines()
        for info in data[1:]:
            id_case, date, code, city, departament, attention, age, sex, tipo, state, precedence = info.split(',')[:11]
            Covid(id_caso=id_case, fecha_diagnostico=date, ciudad_ubicacion=city,
                  departamento=departament, atencion=attention, edad=age, sexo=sex,
                  tipo=tipo, pais_procedencia=precedence).save()


def get_movies_series():
    req = requests.get(
        'http://finde.latercera.com/series-y-peliculas/que-ver-en-netflix-peliculas-series-buenas-abril-2/')
    info = BeautifulSoup(req.text, 'html.parser')

    info_row = info.find_all('div', attrs={'class': 'bg-white collapse-fix-xs'})

    h2_titles = info_row[0].find_all('h2')[:-2]
    images = info_row[0].select('figure > img')[:-2]

    Movies.drop_collection()
    for title, img in zip(h2_titles, images):
        Movies(title=title.text, url=img.get('src')).save()
