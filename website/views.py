from flask import Blueprint, render_template, url_for, redirect
from .models import Events
from . import db 
from datetime import datetime
from flask_login import login_required, current_user



views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    events = Events.query.all()
    return render_template("home.html", events = events, user = current_user)


@views.route('/<int:event_id>')
def event_details(event_id):
    event = Events.query.get(event_id)
    return render_template("events_details.html", event=event)


from flask import request

@views.route('/select_city', methods=['POST'])
def select_city():
    selected_city = request.form['city']
    return render_template('selected_city.html', city=selected_city)


