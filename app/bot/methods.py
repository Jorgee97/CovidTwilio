from twilio.twiml.messaging_response import MessagingResponse
from ..data.model import DayImage, Covid
from mongoengine.queryset.visitor import Q
from unicodedata import normalize


def clear_string(s: str) -> str:
    return normalize('NFKD', s).encode('ascii', errors='ignore').decode(
        'utf-8')


def list_menu() -> str:
    return response_builder(f"""
    Bienvenid@ a COVID19 Info
    Este es nuestro menu:
    0: Lineas MinSalud
    1: Grafico Situación Actual
    2: Resumen
    Filtro por ciudad o departamento (Ej, Bogota)
    """)


def select_menu_option(option: str, options: dict) -> str:
    return options.get(option, default_response())


def information_numbers() -> str:
    return response_builder(f"""
    Líneas MinSalud
    Nacional: 018000955590
    Bogotá: 3305041
    Desde Celular: 192""")


def information_graphic() -> str:
    images = DayImage.objects.order_by('-id').first()
    if images is None:
        return response_builder("Lo sentimos, no hemos encontrado información.")
    return response_builder(images.title, images.url)
    

def information_filter(city_or_state: str = "") -> str:
    city_or_state = clear_string(city_or_state)
    covid = Covid.objects(Q(ciudad_ubicacion__contains=city_or_state) | Q(departamento__contains=city_or_state))

    print(city_or_state)

    if covid is None or len(covid) == 0:
        return default_response()
    return response_builder(f"Total {len(covid)}")


def default_response() -> str:
    return response_builder("""Opción no soportada, lo sentimos por el inconveniente, envia "menu" para mostrar las 
    opciones.""")


def response_builder(message: str, media: str = None) -> str:
    response = MessagingResponse()
    outgoing_message = response.message()

    outgoing_message.body(message)

    if media is not None:
        outgoing_message.media(media)

    return str(response)
