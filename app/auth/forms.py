from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import sqlalchemy as sa
from app import db
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя',
                           validators=[DataRequired('Это поле нужно заполнить!')])
    password = PasswordField('Пароль',
                             validators=[DataRequired('Это поле нужно заполнить!')])
    remember_me = BooleanField('Запомнить', default=True)
    submit = SubmitField('Войти')


class RegistrationForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired('Это поле нужно заполнить!')])
    email = StringField('Email',
                        validators=[DataRequired('Это поле нужно заполнить!'), Email('Некорректный email')])
    password = PasswordField('Пароль', validators=[DataRequired('Это поле нужно заполнить!')])
    password2 = PasswordField('Пароль повторно',
                              validators=[DataRequired('Это поле нужно заполнить!'),
                                          EqualTo('password', 'Пароли должны совпадать!')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(
            User.username == username.data))
        if user is not None:
            raise ValidationError('Это имя занято, введите другое имя.')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(
            User.email == email.data))
        if user is not None:
            raise ValidationError('Этот email занят, введите другой.')
