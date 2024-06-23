from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Имя',
                           validators=[DataRequired('Это поле нужно заполнить!')])
    password = PasswordField('Пароль',
                             validators=[DataRequired('Это поле нужно заполнить!')])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')
