from flask import Blueprint, render_template

from service import config
from service.parse import weather

weather_app = Blueprint('weather_app', __name__)

page_title = 'WEB TRACK LP24'


@weather_app.route('/')
def index():
    city = 'Barnaul,Russia'
    city, current_weather = weather.get_weather(city)
    return render_template(
        'index.html',
        page_title=config.PAGE_TITLE,
        city=city,
        weather_text=current_weather,
    )
