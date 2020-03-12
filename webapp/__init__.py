from flask import Flask, render_template

from webapp.model import db, News
# from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city


def create_app():
    # initialization our application with name 'server'
    app = Flask(__name__)
    # Доступ к переменным в config.py
    app.config.from_pyfile('config.py')
    # Инициализация базы данных
    db.init_app(app)

    # use decorator
    @app.route('/')
    def index():
        title = 'Новости Python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        # news_list = get_python_news()
        # order_by(News.published) - Сортировка по дате.
        # desc() - в обратном порядке
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)
    return app

