from flask import Flask

from service.config import load_from_env
from service.models import db
from service.view.news import news_app
from service.view.weather import weather_app

app_config = load_from_env()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.db_url
    db.init_app(app)

    app.register_blueprint(weather_app, url_prefix='/api/v1/weather')
    app.register_blueprint(news_app, url_prefix='/api/v1/news')

    return app
