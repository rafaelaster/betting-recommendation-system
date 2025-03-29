from website import create_app , db
from flask_restful import Api , Resource , reqparse , abort , fields , marshal_with 
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from website.models import User, BettingHistory, Recommendations
from . import db , api , app

user_parser = reqparse.RequestParser()
user_parser.add_argument("username", type=str, required=True)

casino_put_args = reqparse.RequestParser()
casino_put_args.add_argument("game_type", type=str, required=True,
                           help="Game type (slots/poker/blackjack/etc) is required")
casino_put_args.add_argument("amount", type=float, required=True,
                           help="Suggested bet amount is required")
casino_put_args.add_argument("odds", type=float, required=True, help="Odds value is required")

user =  {
        'id': fields.Integer,
        'username': fields.String,
}

bets = {
    'id': fields.Integer,
    'game_type': fields.String,
    'amount': fields.Float,
    'odds': fields.Float, 
    'outcome' : fields.Integer
}

def generate_recommendation(user_id):
    bets = BettingHistory.query.filter_by(user_id=user_id).all()
    if not bets:
        return jsonify("You have to play a game first")
    
    for bet in bets:
        if bet.odds < 0.3 and bet.amount > 100:
            high_risk = bet
        if bet.odds > 0.6 and bet.amount == 30 :
            moderate_play = bet
        if bet.odds > 0.9 and bet.amount == 70 :
            conservative_play = bet
    if high_risk:
        return "slotslust"
    elif moderate_play:
        return "seriousjacker"
    elif conservative_play:
        return "scaredpokerman"
    return jsonify("No recommendation")

class User(Resource):
    @marshal_with(user)
    def post(self):
        args = user_parser.parse_args()
        if User.query.filter_by(username = args['username']).first():
            abort(409, message="Username already exists")
        user = User(username=args['username'])
        db.session.add(user)
        db.session.commit()
        return jsonify(user)

    
class Bet(Resource):
    @marshal_with(bets)
    def post(self , user_id):
        user = User.query.get(user_id)
        if not user:
            abort(404, message="User not found")
            
        args = casino_put_args.parse_args()
        bet = BettingHistory(
            user_id=user_id,
            game_type=args['game_type'],
            bet_amount=args['bet_amount'],
            odds=args['odds'],
            outcome=args.get('outcome')
        )
        db.session.add(bet)
        db.session.commit()
        return jsonify(bet)
    
class Recommendation(Resource):
    def get(self , user_id):
        user = User.query.get(user_id)
        if not user:
                abort(404, message = "Could not find user")
        recommendation = generate_recommendation(user_id)
        db.session.commit()

        return {
            "user_id" : user_id,
            "recommendation" : recommendation,
        }


api.add_resource(User)
api.add_resource(Bet)
api.add_resource(Recommendation)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

 