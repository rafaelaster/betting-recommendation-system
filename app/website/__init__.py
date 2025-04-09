from pathlib import Path
from app import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_restful import Api , Resource
import pymongo
from . import db
from pymongo import MongoClient

# Connecting
lucky_casino = MongoClient("mongodb://localhost:5000/")

users = lucky_casino["users"]
bets = lucky_casino["bets"]
bethistory = lucky_casino["bethistory"]

ultra_luxe = MongoClient("mongodb://localhost:5000/")

users = ultra_luxe["users"]
bets = ultra_luxe["bets"]
bethistory = ultra_luxe["bethistory"]

atomic = MongoClient("mongodb://localhost:5000/")

users = atomic["users"]
bets = atomic["bets"]
bethistory = atomic["bethistory"]

users_lucky = lucky_casino["users_lucky"]

lucky_casino.arbiters
# api = Api()
# DB_NAME = "database.db"


# def create_app():
#     app = Flask(__name__)
#     app.config['SECRET_KEY'] = 'NANAHACHILOL'

#     db.init_app(app)
#     api.init_app(app)

#     from .models import User
#     create_database(app)
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
    

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         with app.app_context():
#             db.create_all()
#             print('Created Database!')

print(client.list_database_names()) 