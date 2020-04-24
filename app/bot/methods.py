from random import randrange
from unicodedata import normalize
from flask import Response
from twilio.twiml.messaging_response import MessagingResponse
from ..data.model import DayImage, Covid, Movies
from mongoengine.queryset.visitor import Q


def clear_string(s: str) -> str:
    return normalize('NFKD', s).encode('ascii', errors='ignore').decode(
        'utf-8')


def list_menu(not_found: str = "") -> str:
    return response_builder(f"""
    {not_found}
    Bienvenid@ a COVID19 Info
    Este es nuestro menu:
    0: Lineas MinSalud Colombia
    1: Grafico Situación Actual Colombia
    2: Resumen COVID19 Colombia
    3: Recomendacion de peliculas o series (Aleatorio)

    Si desea filtrar por ciudad o departamento, digite:
    (Ej, Cali, Barranquilla)

    NOTA: Si desea buscar casos en Bogota, por favor digite Bogota d.c.

    """)


def select_menu_option(option: str, options: dict) -> str:
    return options.get(option, default_response())()


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
    covid = Covid.objects(Q(ciudad_ubicacion__exact=city_or_state) | Q(departamento__exact=city_or_state))
    if covid is None or len(covid) == 0:
        return default_response()
    response = f"Casos en *{city_or_state.capitalize()}: {len(covid)} en total* \n"
    status_patients = covid.aggregate([{
        '$group': {'_id': "$atencion", 'cases': {'$sum': 1}}
    }])

    for case in list(status_patients):
        response += f"*{case['_id'].capitalize()}*: {case['cases']} \n"

    return response_builder(response)


def information_total() -> str:
    response = f"Casos en *Colombia* \n"
    covid = Covid.objects().aggregate([
        {
            '$group': {'_id': "$atencion", 'cases': {'$sum': 1}}
        }
    ])
    for case in list(covid):
        response += f"*{case['_id'].capitalize()}*: {case['cases']} \n"
    return response_builder(response)


def get_random_movie_or_series() -> Response:
    movies = Movies.objects
    random_int = randrange(0, len(movies), 3)
    random_movie = movies[random_int]
    print("Calling random")
    return response_builder_headers(random_movie.title, random_movie.url)


def default_response() -> str:
    response = "No hemos encontrado informacion, por favor intenta nuevamente"
    return list_menu(response)


def response_builder_headers(message: str, media: str = None) -> Response:
    response = MessagingResponse()
    outgoing_message = response.message()

    outgoing_message.body(message.strip())

    if media is not None:
        outgoing_message.media(media)

    return Response(headers={'Cache-Control': 'no-cache, max-age=0, no-store'}, response=str(response))


def response_builder(message: str, media: str = None) -> str:
    response = MessagingResponse()
    outgoing_message = response.message()

    outgoing_message.body(message.strip())

    if media is not None:
        outgoing_message.media(media)
    return str(response)
