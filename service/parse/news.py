from pathlib import Path

import requests
from bs4 import BeautifulSoup

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

    def __init__(self, url):
        super().__init__(url)

    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        ul_block = soup.find('ul', class_='list-recent-posts')
        h3_block = ul_block.find_all('h3')
        return [block.get_text() for block in h3_block]
