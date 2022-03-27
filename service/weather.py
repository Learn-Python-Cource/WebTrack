import requests


def weather_by_city(city_name):
    weather_url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': '4375ed2187ac4207a4a62831222703',
        'q': city_name,
        'format': 'json',
        'num_of_days': 1,
        'lang': 'ru',
    }
    result = requests.get(weather_url, params=params)
    return result.json()


def get_weather(city_name):
    weather = weather_by_city(city_name)

    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except (IndexError, TypeError):
                return False
    return False
