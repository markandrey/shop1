from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    products = [
        {
            'manufactured': {'title': 'Nike'},
            'name': 'Штора1',
            'photo': 'Фото1.1',
            'vendor_code': 12345,
            'quantity': 100,
            'price': 100,
        },
        {
            'manufactured': {'title': 'Adidas'},
            'name': 'Карниз1',
            'photo': 'Фото1.2',
            'vendor_code': 23456,
            'quantity': 100,
            'price': 300,
        }
    ]
    return render_template('index.html',
                           title='Главная',
                           user=user,
                           products=products,
                           )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Пользователь {} вошел, запомнить = {}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',
                           title='Войти',
                           form=form,
                           )
