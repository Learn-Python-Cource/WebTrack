import requests

from service.config import WEATHER_API_KEY, WEATHER_DEFAULT_CITY


def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': WEATHER_API_KEY,
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru',
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        return result.json()
    except (requests.RequestException, ValueError):
        return False


def get_weather(city_name=WEATHER_DEFAULT_CITY):
    weather = weather_by_city(city_name)

    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return city_name, weather['data']['current_condition'][0]
            except (IndexError, TypeError):
                return False
    return False
