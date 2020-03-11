from webapp import db, create_app

# Создание базы
db.create_all(app=create_app())