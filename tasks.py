from celery import Celery
# crontab - модуль для управления расписанием
from celery.schedules import crontab

from webapp import create_app
from webapp.news.parsers import habr

celery_app = Celery('tasks', broker='redis://localhost:6379/0')

flask_app = create_app()


# celery -A tasks worker --loglevel=info - команда для запуска воркера - в командной строке
# func.delay() - вызов функцию с помощью celery - в строке питона
# celery -A tasks beat - команда запуска beat - выполнит "расписание"
# celery -A tasks worker -B --loglevel=info - одновременный запуск воркера и бита (в продакшене не делать)
@celery_app.task
def habr_snippets():
    with flask_app.app_context():
        habr.get_news_snippets()


@celery_app.task
def habr_content():
    with flask_app.app_context():
        habr.get_news_content()


# @celery_app.on_after_configure.connect - подключается и ставит задачи в очередь
@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """Функция задаёт периодичность запуска функции (расписание) - каждую минуту"""
    # .s() - запуск сигнатуры функции
    sender.add_periodic_task(crontab(minute='*/1'), habr_snippets.s())
    sender.add_periodic_task(crontab(minute='*/1'), habr_content.s())