# flash - позволяет передавать сообщения между route-ами (со страницы на страницу)
# redirect - даёт перенаправление пользователя на другую страницу
# url_for - помогает получить url по имени функции, которая этот url обрабатывает
from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required, login_user, logout_user

from webapp.model import db, News, User
from webapp.forms import LoginForm
# from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city


def create_app():
    # initialization our application with name 'server'
    app = Flask(__name__)
    # Доступ к переменным в config.py
    app.config.from_pyfile('config.py')
    # Инициализация базы данных
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    # функция получающая по id объект пользователя
    @login_manager.user_loader
    def load_user(user_id):
        # Запрос к базе данных - получение по id объект пользователя
        return User.query.get(user_id)

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

    @app.route('/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)

    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()

        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))

        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect((url_for('index')))

    @app.route('/admin')
    @login_required
    def admin_index():
        if current_user.is_admin:
            return 'Привет админ!'
        else:
            return 'Ты не админ!'

    return app
