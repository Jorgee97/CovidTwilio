from threading import Thread
from flask import Blueprint, request
from .methods import (information_graphic, clear_string, information_filter, information_numbers, information_total,
                      list_menu, select_menu_option, get_random_movie_or_series)
from ..data.scrapping import get_data, get_day_image, get_movies_series
from ..data.task import scrap_every_day

bot_bp = Blueprint('bot', __package__, url_prefix='/bot')

options = {
    '0': information_numbers,
    '1': information_graphic,
    '2': information_total,
    '3': get_random_movie_or_series
}


@bot_bp.route('', methods=['POST'])
def bot_post():
    incoming_message = request.values.get('Body', '').lower()
    menu = clear_string(incoming_message)
    if incoming_message in options:
        return select_menu_option(incoming_message, options)
    if 'menu' in menu:
        return list_menu()

    return information_filter(incoming_message)


@bot_bp.route('/fetch/data', methods=['GET'])
def bot_fetch_image_manually():
    get_data()
    get_day_image()
    get_movies_series()

    return "Done."


@bot_bp.route('/fetch/random', methods=['GET'])
def bot_fetch_random_movie():
    return get_random_movie_or_series()


@bot_bp.route('/run/task', methods=['GET'])
def bot_run_task():
    thread = Thread(target=scrap_every_day, name="get_data")
    thread.start()

    return "Done!"

