from flask_admin.contrib.sqla import ModelView
from app.models import User
from app import admin, db

admin.add_view(ModelView(User, db.session))
