from flask_sqlalchemy import SQLAlchemy

# Инициализация базы данных
db = SQLAlchemy()


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # nullable - может ли быть пустым (проверяет база данных на их наличие)
    title = db.Column(db.String, nullable=False)
    url = db.Column(db.String, unique=True, nullable=False)
    published = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return 'News {} {}'.format(self.title, self.url)
