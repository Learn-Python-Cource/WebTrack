from flask import Blueprint, render_template

from service.config import app_config
from service.repo.news import get_all

view = Blueprint('news', __name__)


@view.route('/')
def py_news():
    my_news = get_all()
    return render_template(
        'news.html',
        page_title=app_config.title,
        news=my_news,
    )
