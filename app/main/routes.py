from flask import render_template, current_app
from app import db
from flask_login import login_required
import sqlalchemy as sa
from app.models import User
from app.main import bp


@bp.route('/')
@bp.route('/index')
def index():
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
                           products=products,
                           )


@bp.route('/user/<username>')
@login_required
def user(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    orders = [
        {
            'order_id': 123,
            'date': '12.06.24',
            'price_total': 1000,
        },
        {
            'order_id': 145,
            'date': '21.06.24',
            'price_total': 5000,
        }
    ]
    return render_template('user.html', user=user, orders=orders)
