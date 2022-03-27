from flask import Flask

from service import weather

app = Flask(__name__)

@app.route('/')
def hello():
    city = 'Barnaul,Russia'
    current_weather = weather.get_weather(city)
    if current_weather:
        answer = f"Сейчас B {city} {current_weather['temp_C']}, ощущается как {current_weather['FeelsLikeC']}"
        return answer
    else:
        return 'Hello!'
