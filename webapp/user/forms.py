from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    # default=True - галочка в чекбоксе по умолчанию отмечена. Поле для "запоминания" пользователя после закрытия сайта
    remember_me = BooleanField('Запомнить меня', default=True, render_kw={"class": "form_check_input"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})