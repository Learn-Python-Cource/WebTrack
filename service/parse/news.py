from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

from service.repo.news import save_news

html_file = Path('service/parse/tmp/python.html')


class UrlReader:

    def __init__(self, url):
        self.url = url
        self.html = self._news_parser()

    def _get_news(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except (requests.RequestException, ValueError):
            return False

    def _news_parser(self):
        html = self._get_news()
        if html:
            with open(html_file, 'w', encoding='utf-8') as file_html:
                file_html.write(html)
            return html
        return 'download error'


class SoupParser(UrlReader):

    def __init__(self, url):  # noqa: WPS612
        super().__init__(url)

    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        ul_block = soup.find('ul', class_='list-recent-posts').find_all('li')
        result_news = []
        for news in ul_block:
            title = news.find('a').text
            url = news.find('a')['href']
            published = news.find('time').text
            try:
                published = datetime.strptime(published, '%Y-%m-%d')
            except ValueError:
                published = datetime.now()
            save_news(
                title=title,
                url=url,
                published=published,
            )
            result_news.append({
                'title': title,
                'url': url,
                'published': published,
            })

        return result_news
