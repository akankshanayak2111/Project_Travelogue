"""Flight Details."""

from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Trips
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

@app.route('/origin-budget.json')
def origin_budget_data():
    """Return data about average budgets."""
    origin_list = db.session.query(Trips.origin).all()
    origin = set(origin_list)
    origin_data = list(origin)
    budget_data = []
    for o in origin:
        avg =   db.session.query(db.func.avg(Trips.budget)).filter(Trips.origin == o).first()
        budget_data.append(avg)
    budget_data = set(budget_data)
    budget = list(budget_data)
    budget_list = []
    for val in budget:
        for v in val:
            t = int(v)
            budget_list.append(t)
    

    color = ["#4747d1", "#ff80aa", "#ff944d", "#70db70", "#36A2EB", "#FF6384", "#F7464A", "#46BFBD", "#949FB1", "#4D5360", "#80ffff"]
    data_dict = {
                "labels": [
                    o for o in origin_data
                ],
                "datasets": [
                    {
                        "data": [b for b in budget_list],
                        "backgroundColor": [
                            c for c in color
                        ],
                        "hoverBackgroundColor": [
                            c for c in color
                        ]
                    }]
            }

    

    return jsonify(data_dict)



@app.route('/destinations')
def show_destinations():
    """Returns the destinations based on user's search criteria."""

    origin = request.args.get("origin")
    user_budget = request.args.get("budget")
    date_start = request.args.get("start-date")
    date_return = request.args.get("return-date")
    passenger = request.args.get("passengers")


    #Using Money python package to format the user_budget field in ISO-4217 format for sending API request
    budget = Money(user_budget, 'USD')
    budget = budget.currency + str(budget.amount)



    
    if 'user' not in session:
        session.clear()
    global all_flights
    all_flights = make_request(origin, budget, date_start, date_return, passenger)
    # all_flights = session['all_flights']
    
    # all_flights = session['all_flights']


    session['origin'] = origin
    session['budget'] = user_budget
    session['date_start'] = date_start
    session['date_return'] = date_return
    session['passenger'] = passenger
    

   
    # destinations_display = display_destinations(all_flights)
    session['destinations_display'] = display_destinations(all_flights)
    
    destinations_display = session['destinations_display']
    user_dest = session['destinations_display']
    # print destinations_display

    
    return render_template("destinations.html", destinations=destinations_display, user_dest=json.dumps(user_dest))

@app.route('/flight_details/<dest>')
def show_flights(dest):
    """Returns the flights for each destination."""
    # if 'user' not in session:
    #     session.clear()
    # all_flights = session['all_flights']
    
    # all_flights = session['all_flights']
   
    # print session['all_flights'].keys()

    
    flight_results = get_flight_details(dest, all_flights)

    print flight_results
    
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
        session.clear()
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
    # session['user'] = user
    
    # user_trips = user.trips

    return render_template("user.html", user=user)


@app.route('/trips')
def show_searched_trips():
    """Shows the user's searched trips."""

    budget = session['budget']
    origin = session['origin']
    start_date = session['date_start']
    return_date = session['date_return']
    user_id = session['user']
    dest = session['destinations_display']
    user = User.query.get(user_id)
    
   


    if user_id:
        trip = Trips(user_id=user_id,budget=budget,origin=origin,dest=dest,date_started_at=start_date,date_returned_at=return_date)
    
        db.session.add(trip)
    
    db.session.commit()


    return render_template("trips.html", trip=trip, user=user)


@app.route('/logout')
def logout():
    """Log out."""

    session.clear()
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