from flask import Blueprint, render_template

from service import config
from service.parse import news

news_app = Blueprint('news_app', __name__)


@news_app.route('/')
def py_news():
    url = 'https://www.python.org/blogs/'
    current_news = news.SoupParser(url)
    return render_template(
        'news.html',
        page_title=config.PAGE_TITLE,
        news=current_news.get_python_news(),
    )
