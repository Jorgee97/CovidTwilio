from twilio.twiml.messaging_response import MessagingResponse

def list_menu() -> str:
    return response_builder(f"""
    Bienvenid@ a COVID19 Info
    Este es nuestro menu:
    0: Lineas MinSalud
    1: Grafico Situación Actual
    2:""")


def select_menu_option(option: str, options: dict) -> str:
    return options.get(option, default_response())


def information_numbers() -> str:
    return response_builder(f"""
    Líneas MinSalud
    Nacional: 018000955590
    Bogotá: 3305041
    Desde Celular: 192""")


def information_graphic() -> str:
    return response_builder("Este es el grafico del día", 
    "https://www.minsalud.gov.co/salud/publica/PET/PublishingImages/covid-19%20Colombia/040420_post_coronavirus_baja.jpg")


def default_response() -> str:
    return response_builder("""Opción no soportada, lo sentimos por el inconveniente, envia "menu" para mostrar las opciones.""")


def response_builder(message: str, media: str = None) -> str:
    response = MessagingResponse()
    outgoing_message = response.message()

    outgoing_message.body(message)

    if media is not None:
        outgoing_message.media(media)

    return str(response)
