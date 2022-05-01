from flask import Flask

from service.config import load_from_env
from service.models import db
from service.views import login, news, weather

app_config = load_from_env()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.db_url
    app.config['SECRET_KEY'] = app_config.secret_key
    db.init_app(app)

    app.register_blueprint(login.view, url_prefix='/login')
    app.register_blueprint(news.view, url_prefix='/news')
    app.register_blueprint(weather.view, url_prefix='/weather')

    return app
