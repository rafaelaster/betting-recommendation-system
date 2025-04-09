from functools import wraps
from wsgiref import validate
from xml.dom import ValidationErr
from app import Blueprint , render_template
from app.website.schemas import RECOMMENDATION_SC
from .models import users, coupons, events , clients
from flask import Flask, jsonify, request

views = Blueprint('views' , __name__ )

@views.route('/')
def home():
    return render_template("home.html")

  #  try:
        

@views.route('recommendation/<int:user_id>' , methods = ['GET'])
def get_recommendation(user_id):
    
    config = clients.find_one({"user_id": user_id})

    if config["recommender_type"] == "Static":
        recommendations = config["config" , "recommendations"]
    if not config:
        return jsonify({"error": "No configuration found"}), 404
    
    user = users.find_one({"user_id": user_id})

    recommendations = []

    if config["recommender_type"] == "Static":
        # Return static recommendations from config
        recommendations = config["config"]["recommendations"]


    events = list(events.find(base_query).limit(10))

    recommendations = [{
        RECOMMENDATION_SC
    }]


def validate_schema(schema):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json()
                validate(instance=data, schema=schema)
                return f(*args, **kwargs)
            except ValidationErr as e:
                return jsonify({"error": e.message}), 400
        return wrapper
    return decorator


@views.route('</config/' , methods = ['POST'])
@validate_schema(RECOMMENDATION_SC) 
def modificate_config(recommender):
    #not validating schema 
    data = request.get_recommendation   
    if 'type' not in data:
        return jsonify({"error": "Missing schema type"}), 400
    
    schema_type = data['type']

    if schema_type == "Static":
        return generate_recommendation(data['recommendations'])
    elif schema_type == "Dynamic":
        return generate_recommendation(data['rules'])  
    

def generate_recommendation():
    