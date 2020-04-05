from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse

bot_bp = Blueprint('bot', __package__, url_prefix='/bot')


@bot_bp.route('', methods=['POST'])
def bot_post():
    incoming_message = request.values.get('Body', '').lower()
    response = MessagingResponse()
    message = response.message()

    message.body(f'Hey, you send me this message {incoming_message}')

    return str(response)