import time
from .scrapping import get_data, get_movies_series, get_day_image

SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24

while True:
    get_data()
    get_day_image()
    get_movies_series()
    time.sleep(SECONDS_PER_HOUR*HOURS_PER_DAY)
