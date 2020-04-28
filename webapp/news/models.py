from datetime import datetime
# relationship - для удобства связии данных
from sqlalchemy.orm import relationship

from webapp.db import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # nullable - может ли быть пустым (проверяет база данных на их наличие)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def comments_count(self):
        """Количество комментариев к новости"""
        return Comment.query.filter(Comment.news_id == self.id).count()

    def __repr__(self):
        return 'News {} {}'.format(self.title, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    news_id = db.Column(
        db.Integer,
        # ondelete='CASCADE' - поведение при удалении (если удалить новость, удалятся все комменты к ней)
        # нельзя будет удалить новость, пока не удалить все комментарии к ней
        db.ForeignKey('news.id', ondelete='CASCADE'),
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )

    # news - виртуальное поле которое ссылается на модель News, которая будет выглядеть как comments
    # from webapp.news.models import Comment
    # c = Comment.query.get(1)
    # c.user --> <User Kostya, id=1)
    # c.news
    # News Микросервисы на Java: практическое руководство https://habr.com/ru/post/491556/
    # c.news.title
    # Микросервисы на Java: практическое руководство

    # from webapp.news.models import News
    # news = News.query.get(3)
    # news.comments[0].text
    # news.comments
    # [<Comment 1>]
    # 'Проверка связи'
    news = relationship('News', backref='comments')
    user = relationship('User', backref='comments')

    def __repr__(self):
        return '<Comment {}>'.format(self.id)
