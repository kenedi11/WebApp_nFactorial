from flask import Blueprint, render_template, flash, url_for, redirect
from .models import Events, SavedEvents
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


@views.route('/save', methods = ['POST'])
def save():
    event_id = request.form.get('event_id')
    saved_event = SavedEvents.query.filter_by(user_id=current_user.id, event_id=event_id).first()
    if saved_event:
        flash('Уже в сохранненых!', category = 'warning')

    saved_event = SavedEvents(user_id=current_user.id, event_id=event_id)
    db.session.add(saved_event)
    db.session.commit()

    flash('Ивент сохранен успешно!', category='success')
    
    return redirect(url_for('views.home'))


@views.route('/saved', methods = ['GET'])
@login_required
def saved():
    saved_events = SavedEvents.query.filter_by(user_id=current_user.id).all()

    event_ids = [saved_event.event_id for saved_event in saved_events]

    events = Events.query.filter(Events.id.in_(event_ids)).all()

    return render_template("saved.html", events=events)

@views.route('/select_city', methods=['POST', 'GET'])
def select_city():
    if request.method == 'POST':
        selected_city = request.form['city']
        events_city = Events.query.filter(Events.city == selected_city).all()
        return render_template('selected_city.html', city=selected_city, events=events_city)
    else:
        return render_template('home.html')
