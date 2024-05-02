from . import db 
from sqlalchemy.sql import func
from datetime import datetime
from flask_login import UserMixin


class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    event_date = db.Column(db.String(5), nullable=False)    
    organizer = db.Column(db.String(100))
    category = db.Column(db.String(50))
    registration_deadline = db.Column(db.DateTime)
    price = db.Column(db.Integer)
    img_url = db.Column(db.String(255))

    def __init__(self, event_name, description, event_date, location, organizer, category, price):
        self.event_name = event_name
        self.description = description
        self.event_date = event_date
        self.location = location
        self.organizer = organizer
        self.category = category
        self.price = price


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))


class SavedEvents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('saved_events', lazy=True))
    event = db.relationship('Events', backref=db.backref('saved_by', lazy=True))

    def __init__(self, user_id, event_id):
        self.user_id = user_id
        self.event_id = event_id
