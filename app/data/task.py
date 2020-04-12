import time
import datetime
from .scrapping import get_data
from .scrapping import get_day_image

SECONDS_PER_HOUR = 3600
HOURS_PER_DAY = 24

while True:
    get_data()
    get_day_image()
    time.sleep(SECONDS_PER_HOUR*HOURS_PER_DAY)