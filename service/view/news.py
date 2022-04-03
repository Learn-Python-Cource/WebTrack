from flask import Blueprint, render_template

from service import config
from service.parse import news
from service.repo.news import get_all


news_app = Blueprint('news_app', __name__)


@news_app.route('/upload')
def upload_news():
    url = 'https://www.python.org/blogs/'
    current_news = news.SoupParser(url)
    current_news.get_python_news()
    my_news = get_all()
    return render_template(
        'news.html',
        page_title=config.PAGE_TITLE,
        news=my_news,
    )

@news_app.route('/')
def py_news():

    my_news = get_all()

    return render_template(
        'news.html',
        page_title=config.PAGE_TITLE,
        news=my_news,
    )


@news_app.route('/login')
def login():
    title = 'Authorization'
    login_form =
