from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User
import requests
import json
import os
from money import Money
from pprint import pprint



def make_request():
    """Sends request to the API and adds destinations with non-empty response to a list."""

    origin = request.args.get("origin")
    user_budget = request.args.get("budget")
    date_start = request.args.get("start-date")
    date_return = request.args.get("return-date")
    passenger = request.args.get("passengers")

    #Using Money python package to format the user_budget field in ISO-4217 format for sending API request
    budget = Money(user_budget, 'USD')
    budget = budget.currency + str(budget.amount)

    

    access_key = os.environ["FLIGHTS_KEY"]

    destinations = ["ORD", "LAS"]

    
    all_flights = {}

    # Formatting payload according to API request format
    for destination in destinations:
        if destination != origin:
            payload = {
              "request": {
                "passengers": {
                  "adultCount": passenger,
                  "childCount": None,
                  "infantInLapCount": None,
                  "infantInSeatCount": None,
                  "seniorCount": None
                },
                "slice": [
                  {
                    "origin": origin,
                    "destination": destination,
                    "date": date_start,
                    },
                  {
                    "origin": destination,
                    "destination": origin,
                    "date": date_return,
                    },
                ],
                "maxPrice": budget,
                "solutions": 10
              }
            } 

        url = "https://www.googleapis.com/qpxExpress/v1/trips/search?key={}".format(access_key) 



        r = requests.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        global flights
        flights = r.json()
        print flights

        # dict with keys as destination name and values as json for each 
        all_flights[destination] = flights
    print all_flights.keys()
    return all_flights
    


def display_destinations():
    """Displays destinations based on user's search criteria."""
    

    global flights_all_destinations

    flights_all_destinations = make_request()

    # initiating a list of destinations to display
    destinations_display = []

        # check to see if destination json is empty or not
        # if not add destinations destinations_display
    for dest, flights in flights_all_destinations.items():
        if 'tripOption' in flights_all_destinations[dest]['trips']:
            destinations_display.append(dest)
    
    print destinations_display
    return destinations_display



def get_flight_details(dest):
    """Shows flight details for a destination."""  



    #start with json for a destination based on the one clicked
    #massage json to get values to display to the user
    results_destinations = {}
    flight_results =[]

    if dest in flights_all_destinations:
        trip_options = flights_all_destinations[dest]['trips']['tripOption']
        for trip in trip_options:
            round_trip = []
            for flight in trip['slice']:
                flight_info = {}
                flight_info['departure_time'] = flight['segment'][0]['leg'][0]['departureTime']
                flight_info['origin'] = flight['segment'][0]['leg'][0]['origin']
                flight_info['destination'] = flight['segment'][0]['leg'][0]['destination']
                flight_info['carrier'] = flight['segment'][0]['flight']['carrier']
                flight_info['number'] = flight['segment'][0]['flight']['number']
                round_trip.append(flight_info)
            flight_price = {}
            flight_price['price'] = trip['saleTotal']
            round_trip.append(flight_price)
            flight_results.append(round_trip)

    # print flight_results
    return flight_results

    














# def loads_flights_json():
#     """loads json files obtained from the API response."""
#     json_string = open("response.json").read()
#     print json_string

#     flight_dict = json.loads(json_string)
#     pprint(flight_dict)

#     # print flight_dict


# loads_flights_json()
