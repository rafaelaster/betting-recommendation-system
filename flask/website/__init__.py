from pathlib import Path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, login_manager
from flask_restful import Api , Resource

db = SQLAlchemy()
api = Api()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'NANAHACHILOL'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'  # Fixed f-string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    api.init_app(app)

    from .models import User
    create_database(app)
# #  registring my blueprits
#     from .views import views
#     from .auth import auth

#     app.register_blueprint(views , url_prefix = '/' )
#     app.register_blueprint(auth , url_prefix = '/' )
    
#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)

#     #Does the same as filter_by exept it looks for primary key for validation
#     @login_manager.user_loader
#     def load_user(id):
#          return User.query.get(int(id))
    

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')