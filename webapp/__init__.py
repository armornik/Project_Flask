from flask import Flask, render_template

from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city


def create_app():
    # initialization our application with name 'server'
    app = Flask(__name__)


    # use decorator
    @app.route('/')
    def index():
        title = 'Новости Python'
        weather = weather_by_city('Moscow,Russia')
        news_list = get_python_news()
        return render_template('index.html', page_title=title, weather=weather, news_list=news_list)
    return app

