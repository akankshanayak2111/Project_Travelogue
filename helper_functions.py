from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User
import requests
import json
import os
from money import Money
from pprint import pprint
from datetime import datetime
import time



def make_request(origin, budget, date_start, date_return, passenger):
    """Sends request to the API based on user's search criteria."""

    # access_key = os.environ["FLIGHTS_KEY2"]
    access_key = os.environ["FLIGHTS_KEY2"]

    destinations = ["LAS","LAX"]

    
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
        flights = r.json()

        # dict with keys as destination name and values as json for each
        all_flights[destination] = flights
    # print all_flights.keys()
    return all_flights
 


def display_destinations(all_flights):
    """Adds destinations with non-empty response to a list and displays those destinations."""
    
    # initiating a list of destinations to display
    destinations_display = []

        # check to see if destination json is empty or not
        # if not add destinations destinations_display
    for dest, flights in all_flights.iteritems():
        if 'tripOption' in all_flights[dest]['trips']:
            destinations_display.append(dest)
    
    # print destinations_display
    return destinations_display



def get_flight_details(dest, all_flights):
    """Shows flight details for a destination."""  

    #start with json for a destination based on the one clicked
    #massage json to get values to display to the user
   
    flight_results =[]
    # print all_flights[dest]
    if dest in all_flights:
        trip_options = all_flights[dest]['trips']['tripOption']
        for trip in trip_options:
            round_trip = []
            for flight in trip['slice']:
                flight_info = {}
                
                dep_time = flight['segment'][0]['leg'][0]['departureTime']
                time_departure = datetime.strptime(dep_time[:16], '%Y-%m-%dT%H:%M')
                final_time = time_departure.strftime("%Y-%m-%d %H:%M")

                flight_info['departure_time'] = final_time
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
