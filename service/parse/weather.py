from typing import Any

import requests

from service.config import load_from_env

app_config = load_from_env()


def weather_by_city() -> dict[str, Any]:
    weather_url = app_config.weather_url
    params = {
        'appid': app_config.weather_api_key,
        'lat': app_config.weather_city[0],
        'lon': app_config.weather_city[1],
        'units': 'metric',
        'lang': 'ru',
    }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        return result.json()
    except (requests.RequestException, ValueError):
        return {'message': 'false'}


def get_weather(city: str) -> tuple[str, dict[str, Any]]:
    weather = weather_by_city()
    return city, weather.get('main', {'temp': 'нет информации'})
