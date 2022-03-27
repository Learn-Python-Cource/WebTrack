from flask import Flask, render_template

from service.parse import news, weather

app = Flask(__name__)

page_title = 'WEB TRACK LP24'


@app.route('/')
def index():
    city = 'Barnaul,Russia'
    city, current_weather = weather.get_weather(city)
    return render_template(
        'index.html',
        page_title=page_title,
        city=city,
        weather_text=current_weather,
    )


@app.route('/news')
def py_news():
    url = 'https://www.python.org/blogs/'
    current_news = news.SoupParser(url)
    return render_template(
        'news.html',
        page_title=page_title,
        news=current_news.get_python_news(),
    )
