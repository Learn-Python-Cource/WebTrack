from flask import Flask
from flask_login import LoginManager

from service.config import load_from_env
from service.models import User, db
from service.views import login, news, weather

app_config = load_from_env()


def create_app():
    app = Flask(__name__)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    app.config['SQLALCHEMY_DATABASE_URI'] = app_config.db_url
    app.config['SECRET_KEY'] = app_config.secret_key
    db.init_app(app)

    app.register_blueprint(login.view, url_prefix='/login')
    app.register_blueprint(news.view, url_prefix='/news')
    app.register_blueprint(weather.view, url_prefix='/weather')

    return app
