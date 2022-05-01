from flask import Blueprint, render_template

from service.config import app_config
from service.parse import weather

view = Blueprint('weather_app', __name__)


@view.route('/')
def index():
    city = 'Barnaul'
    city, current_weather = weather.get_weather(city)
    return render_template(
        'index.html',
        page_title=app_config.title,
        city=city,
        weather_text=current_weather,
    )
