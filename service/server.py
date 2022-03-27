from flask import Flask, render_template

from service import weather

app = Flask(__name__)


@app.route('/')
def index():
    city = 'Barnaul,Russia'
    current_weather = weather.get_weather(city)
    if current_weather:
        return render_template(
            'index.html',
            city=city,
            weather_text=current_weather,
        )
    return 'Hello!'
