from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from .methods import *
from ..data.scrapping import get_data

bot_bp = Blueprint('bot', __package__, url_prefix='/bot')

options = {
    '0': information_numbers(),
    '1': information_graphic(),
    '2': 'Option 2',
    '3': 'Option 3',
}


@bot_bp.route('', methods=['POST'])
def bot_post():
    incoming_message = request.values.get('Body', '').lower()

    if incoming_message in options:
        return select_menu_option(incoming_message, options)
    if 'menu' in incoming_message:
        return list_menu()

    return default_response()

