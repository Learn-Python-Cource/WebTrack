from flask import Blueprint, render_template

from service.config import app_config
from service.repo.news import get_all

news_app = Blueprint('news_app', __name__)


@news_app.route('/')
def py_news():
    my_news = get_all()
    return render_template(
        'news.html',
        page_title=app_config.title,
        news=my_news,
    )
