from urllib import response
from flask import Flask, app, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from pydantic import BaseModel, ValidationError
from models import db , User , Client , Coupon , Recommendation


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:2003@localhost/db'

db.init_app(app)


def format_coupons(coupons, schema):
    formatted = []
    for coupon in coupons:
        item = {}
        for field, source in schema.items():
            if source.startswith('attributes.'):
                attr_key = source.split('.', 1)[1]
                item[field] = coupon.attributes.get(attr_key)
            else:
                item[field] = getattr(coupon, source, None)
        formatted.append(item)
    return formatted

@app.route('/<int:client_id>/<username>', methods=['GET'])
def get_recommendations(client_id, username):
    user = User.query.filter_by(username=username, client_id=client_id).first()
    
    if not user:
        return jsonify({"error": "User not found for this client"}), 404
    
    recommendations = Recommendation.query.filter_by(user_id=user.id).first()
    
    if not recommendations:
        return jsonify({"error": "No recommendations found"}), 404
    return jsonify({
        
        "username": user.username,
        "client_id": client_id,
        "recommendations": recommendations.recommendation_set
    })

@app.route('/config/<int:client_id>', methods=['POST'])
def generate_configuration(client_id):
   data = request.get_json()
   client = Client.query.get(client_id)

   if not client:
      return jsonify({"message": "Unable to find client "}), 404
   client.schema = data
   db.session.commit()
   return jsonify({"message": "Configuration updated successfully"}), 200




if __name__ == "__main__":
     with app.app_context():
        db.create_all()
     app.run(debug=True)







    











