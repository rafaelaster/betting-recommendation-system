from dataclasses import Field
from typing import Any, List, Optional
from bson import ObjectId
from datetime import datetime
from sqlalchemy import Column, Integer
from sqlalchemy.types import JSON
from sqlalchemy import Column, Integer, String , ARRAY
from pydantic import BaseModel, Json, PostgresDsn, ValidationError, field_validator 
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, nullable=False, unique=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    client = db.relationship('Client', back_populates='users')  # Changed to 'users'
    recommendations = db.relationship('Recommendation', back_populates='user')

class Client(db.Model):
    __tablename__ = 'clients'
    client_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    schema = db.Column(db.JSON)
    users = db.relationship('User', back_populates='client')  # This is correct
    coupons = db.relationship('Coupon', back_populates='client')

class Coupon(db.Model):
    __tablename__ = 'coupons'
    coupon_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    coupon_name = db.Column(db.String(50))
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    client = db.relationship('Client', back_populates='coupons')  # Fixed relationship
    attributes = db.Column(db.JSON)

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    event_name = db.Column(db.String(50))
    event_type = db.Column(db.String(50))
    event_group = db.Column(db.String(50))


class Recommendation(db.Model):  # Changed to singular
    __tablename__ = 'recommendations'
    recommendation_id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    recommendation_set = db.Column(db.ARRAY(db.JSON))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='recommendations')




