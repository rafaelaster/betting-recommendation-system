import pymongo
from . import db




client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB URI
db = client['my_project_db']  

users = db['users']
coupons = db['coupons']
events = db['events']
clients = db['clients']
recommendations = db['recommendations']

db.clients.insert_many({
    "client_id" : "2003doom",
    "client_name" : "atomic-wrengler",
    "users" : 100
})


db.events.insert_many({

})
db.users.insert_many({
      "user_id" : 
       "2003coolkid"
    ,
    "username": "rafaelaster"
},
{
      "user_id" : 
       "kitten2090"
    ,
    "username": "falloutboy"
},{
    "user_id" : "russian2"
    ,
    "username": "amigo"
})

    # def __repr__(self):
    #     return f'''Casino Recommendation(
    #         game={self.game_type}, 
    #         recommendation={self.recommendation}
    #     )'''
    
