import requests
from bs4 import BeautifulSoup
from .model import DayImage
from flask import Blueprint, request, Response
import pandas as pd
from sodapy import Socrata

scrap_bp = Blueprint('scrap', __package__, url_prefix='/scrap')

def get_day_image():
    r = requests.get('https://www.minsalud.gov.co/salud/publica/PET/Paginas/Covid-19_copia.aspx')
    soup = BeautifulSoup(r.text, 'html.parser')

    resultsRow = soup.find_all('div', attrs={'id': 'WebPartWPQ4'})

    results = []

    for resultRow in resultsRow:
        text = "Imagen del dia"
        img = resultRow.find('img').get('src')
    
        results.append({
            'text': text,
            'img': img
        })
    save_data_image(results)


def save_data_image(data: list):
    DayImage(title=data[0].text, url=data[0].img).save()


def get_data():
    client = Socrata("www.datos.gov.co", None)
    results = client.get("gt2j-8ykr", limit=2000)
    results_df = pd.DataFrame.from_records(results)
    print(results_df)