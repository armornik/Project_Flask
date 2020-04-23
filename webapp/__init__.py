# flash - позволяет передавать сообщения между route-ами (со страницы на страницу)
# redirect - даёт перенаправление пользователя на другую страницу
# url_for - помогает получить url по имени функции, которая этот url обрабатывает
from flask import Flask
from flask_login import LoginManager

from webapp.db import db
from webapp.admin.views import blueprint as admin_blueprint
from webapp.news.views import blueprint as news_blueprint
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint


def create_app():
    # initialization our application with name 'server'
    app = Flask(__name__)
    # Доступ к переменным в config.py
    app.config.from_pyfile('config.py')
    # Инициализация базы данных
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    app.register_blueprint(user_blueprint)

    # функция получающая по id объект пользователя
    @login_manager.user_loader
    def load_user(user_id):
        # Запрос к базе данных - получение по id объект пользователя
        return User.query.get(user_id)

    return app
