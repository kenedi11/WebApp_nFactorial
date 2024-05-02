from . import db 
from sqlalchemy.sql import func
from datetime import datetime
from flask_login import UserMixin


class Events(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    event_name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    event_datetime = db.Column(db.DateTime(timezone = True), nullable=False, default = func.now())
    organizer = db.Column(db.String(100))
    category = db.Column(db.String(50))
    registration_deadline = db.Column(db.DateTime)
    price = db.Column(db.Float)
    img_url = db.Column(db.String(255))

    def __init__(self, event_name, description, event_datetime, location, organizer, category, price):
        self.event_name = event_name
        self.description = description
        self.event_datetime = event_datetime
        self.location = location
        self.organizer = organizer
        self.category = category
        self.price = price





class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
