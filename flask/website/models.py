from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    bets = db.relationship('BetHistory', backref='user', lazy=True)


class BettingHistory(db.Model):
    bet_id = db.Column(db.Integer , primary_key = True )
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    game_id =  db.relationship(db.Integer, back_populates=('bet.id'))
    game_type = db.Column(db.String(50) , nullable = False)
    amount = db.Column(db.Float, nullable=False)
    odds = db.Column(db.Float)
    outcome = db.Column(db.Integer(50))

class Recommendations(db.Model):
    rec_id = db.Columnn(db.Integer , primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id') , nullable = False)
    bet_id = db.Column(db.Integer, db.ForeignKey('bet.id'), nullable=False)
    recommendation_name = db.Column(db.String(100), nullable=False)


    # def __repr__(self):
    #     return f'''Casino Recommendation(
    #         game={self.game_type}, 
    #         recommendation={self.recommendation}
    #     )'''
    
