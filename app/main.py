from website import  db
from flask_restful import Api , Resource , reqparse , abort , fields , marshal_with 
from flask_sqlalchemy import SQLAlchemy
from app import Flask, jsonify
from website.models import User, BettingHistory, Recommendations
from . import db , api , app
from markupsafe import escape
from pymongo import MongoClient
from bson.objectid import ObjectId
import socket 
import app
from models import recommendations , events , clients , coupons , users
client = MongoClient("mongodb://localhost:5000/")
# db = client.recommendations


# users = db["users"]

# users = [
#     {
#         "user_id" : "2323",
#         "bets" : "10",
#         "username" : "bill"
#     },
#         {
#         "user_id" : "4543",
#         "bets" : "2",
#         "username" : "leo"
#     }
# ]

# bets = db["bets"]

# recommendations = db["recommendations"]



# recommendations = [
#     {
#       "casinogame": "Roulette",
#       "betType": "Even Money Bet",
#       "risklvl": "low to medium",
#       "odds": "1:1"
#     },
#     {
#       "casinogame": "Blackjack",
#       "betType": "Basic Strategy Bet",
#       "risklvl": "low",
#       "odds": "1:1 "   
#     },
#     {
#       "casinogame": "Craps",
#       "betType": "Pass Line Bet",
#       "risklvl": "Low to Medium",
#       "odds": "1:1"
#     }
# ]


# @app.route('/<recommendation_id>/clients')
# def send(msg):
#     message = msg.encode(format)
#     msg_length = len(message)
#     #its the first message that we send and we need to ensure that this message is 64 bytes long (header size)
#     send_length = str(msg_length).encode(format)
#     send_length += b' ' * (header - len(send_length))
#     client.send(send_length)
#     client.send(message)
#     print(client.recv(2048).decode(format))

app = Flask(__name__)

@app.route("/")
def home():
    return f"Container ID: {socket.gethostname()}"

clients = db['clients']
class RecommendationRequest(clients , users):




if __name__ == "__name__":
    app.run(debug=True)