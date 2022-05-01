from service.models import News, db


def get_all():
    return News.query.order_by(News.published.desc()).all()


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(
            title=title,
            url=url,
            published=published,
        )
        db.session.add(new_news)
        db.session.commit()
