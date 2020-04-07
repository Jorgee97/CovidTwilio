import requests
from bs4 import BeautifulSoup


def get_day_image() -> list:
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
    return results

