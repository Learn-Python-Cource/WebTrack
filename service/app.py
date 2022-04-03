from flask import Flask

from service.models import db
from service.view.news import news_app
from service.view.weather import weather_app


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    app.register_blueprint(weather_app, url_prefix='/api/v1/weather')
    app.register_blueprint(news_app, url_prefix='/api/v1/news')

    return app
