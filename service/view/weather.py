from flask import Blueprint, render_template

from service.config import load_from_env
from service.parse import weather

weather_app = Blueprint('weather_app', __name__)

app_config = load_from_env()


@weather_app.route('/')
def index():
    city = 'Barnaul'
    city, current_weather = weather.get_weather(city)
    return render_template(
        'index.html',
        page_title=app_config.title,
        city=city,
        weather_text=current_weather,
    )
