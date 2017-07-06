"""Flight Details."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User
import requests
import json
import os
from money import Money
from helper_functions import make_request, display_destinations, get_flight_details


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


app.jinja_env.undefined = StrictUndefined





@app.route('/')
def index():
    """Form that allows user to enter search criteria."""

    return render_template("homepage.html")



@app.route('/destinations')
def show_destinations():
    """Returns the destinations based on user's search criteria."""

    session['all_flights'] = make_request()
    all_flights = session['all_flights']

    destinations_display = display_destinations(all_flights)
    return render_template("destinations.html", destinations=destinations_display)


@app.route('/flight_details/<dest>')
def show_flights(dest):
    """Returns the flights for each destination."""

    all_flights = session['all_flights']
    
    flight_results = get_flight_details(dest, all_flights)
 
    # flights_sorted = sorted(flights, key=lambda k: k['cost'])
    return render_template("flight_details.html", flight_results=flight_results)


@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup."""

    return render_template("register_form.html")


@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    # Get form variables
    first_name = request.form.get("first-name")
    last_name = request.form.get("last-name")
    email = request.form.get("email")
    password = request.form.get("password")

    if User.query.filter(User.email == email).first():
        flash('Email already exists, please login.')

    else:
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash('Successfully registered new user, please login.')

    return redirect("/login")




@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    # Get form variables
    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter(User.email == email).first()

    if user and user.password == password:
        session['user'] = user.user_id
        flash('Logged in')
        return redirect("/users/{}".format(user.user_id))
    else:
        flash('Incorrect email/password')
        return redirect("/login")


@app.route("/users/<int:user_id>")
def user_detail(user_id):
    """Show info about user."""

    user = User.query.get(user_id)
    user_trips = user.trips

    return render_template("user.html", user=user,
                            user_trips=user_trips)


@app.route('/logout')
def logout():
    """Log out."""

    session.pop('user')
    flash('Logged out')

    return redirect("/")





if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
