from flask import Flask

from service import weather

app = Flask(__name__)


@app.route('/')
def hello():
    city = 'Barnaul,Russia'
    current_weather = weather.get_weather(city)
    if current_weather:
        return 'Сейчас B {0} {1}, ощущается как {2}'.format(
            city,
            current_weather['temp_C'],
            current_weather['FeelsLikeC'],
        )
    return 'Hello!'
