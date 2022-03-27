import requests
from pathlib import Path

html_file = Path('service/parse/tmp/python.html')


class UrlReader:

    def __init__(self, url):
        self.url =url

    def get_news(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Сетевая ошибка')
            return False

    def news_parser(self):
        html = self.get_news()
        if html:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html)
            return 'html text download'
        return 'download error'


class SoupParser(UrlReader):
    pass
