USER_SC = {
  "$id": "https://example.com/user-profile.schema.json",
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "description": "A representation of a user profile",
  "type": "object",
  "required": ["username", "user_id" ],
  "properties": {
    "user_id" : {
        "type" : "string",
        "format" : "string"
    },
    "username": {
      "type": "string"
    }
  }
}
EVENT_SC = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "begin_timestamp": {"type": "string", "format": "date-time"},
        "end_timestamp": {"type": "string", "format": "date-time"},
        "event_id": {"type": "string", "format": "string"},
        "table_id": {"type": "number"},
        "participants": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 2
        },
        "game_type": {"type": "string"},

    },
    "required": ["begin_timestamp", "end_timestamp", "event_id", "table_id", "participants", "game_type"]
}

COUPON_SC = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type" : "object",
    "properties" : {
        "coupon_id" : {"type" : "String" , "format" : "string"},
        "game_type" : {"type" : "String" , "format" : "string"},
        "user_id" : {"type" : "String" , "format" : "String"},
        "suggestions" : {
            "type" : "array",
            "items" : {
                "type" : "object" , 
                "properties" : {
                    "event_id" : {"type" : "string" , "format" : "string"},
                    "odds" : {"type" : "number" , "minimum" : 1.0}
                },
                "required" : ["event_id" , "odds"]
                },
                "minItems" : 1
            },
            "timestamp": {"type": "string", "format": "date-time"},
            "user_id": {"type": "integer"}

        },
        "required": ["coupon_id", "selections", "stake", "timestamp", "user_id"]

}

RECOMMENDATION_SC= {
    "Static" : {
        "type" : "object",
        "properties" : {
            "recommendations" :{
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                         "what": {"type": "string"},
                        "pay": {"type": "number"},
                        "when": {"type": "string", "format": "date"}
                    },
                    "required": ["what", "pay"]
                }
            }
        },
        "required" : ["recommendations"]
    }
}