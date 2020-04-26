import requests

from webapp.db import db
from webapp.news.models import News


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'
    }
    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.text
    except (requests.RequestException, ValueError):
        print(requests.RequestException, ValueError)
        print('Сетевая ошибка')
        return False


def save_news(title, url, published):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:
        new_news = News(title=title, url=url, published=published)
        db.session.add(new_news)
        db.session.commit()

