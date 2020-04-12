from flask import Blueprint, request
from .methods import *
from ..data.scrapping import get_data, get_day_image

bot_bp = Blueprint('bot', __package__, url_prefix='/bot')

options = {
    '0': information_numbers(),
    '1': information_graphic(),
    '2': information_total(),
    '3': information_filter(),
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

    return "Done."
