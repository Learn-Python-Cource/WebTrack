from flask import Blueprint, render_template
from flask_login import current_user, login_required

from service.config import app_config
from service.parse import weather

view = Blueprint('weather', __name__)


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


@view.route('/admin')
@login_required
def admin_page():
    if current_user.is_admin:
        return 'Hello admin!'
