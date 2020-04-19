import time
from .scrapping import get_data, get_movies_series, get_day_image, save_covid_data

SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24


def scrap_every_day():
    get_data()
    save_covid_data()
    get_day_image()
    get_movies_series()
