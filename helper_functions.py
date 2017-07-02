from jinja2 import StrictUndefined

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Movie, Rating
import requests
import json
import os
from money import Money
from pprint import pprint



def make_request():
    """Sends request to the API."""
    origin = request.args.get("origin")
    user_budget = request.args.get("budget")
    budget = Money(user_budget, 'USD')
    budget = budget.currency + str(budget.amount)

    date_start = request.args.get("start-date")
    date_return = request.args.get("return-date")
    passenger = request.args.get("passengers")

    access_key = os.environ["FLIGHTS_KEY1"]
    destinations = ["ORD", "LAX"]

    # all_flights = {}
    destinations_display = []
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
        print flights
        print flights.keys()

        # to store json from each destination in a separate file
        # with open('response_'+destination+'.json', 'w') as outfile:
        #     json.dump(flights, outfile)

        # check to see if destination json is empty or not
        # if not add destinations to a list
        
        if 'tripOption' in flights['trips']:
            destinations_display.append(destination)
    # print destinations_display
    return destinations_display


    # if len(destinations_display) == 0:
    #     return "Sorry no flights matched your search criteria"
    # else:
    #     return destinations_display
    # print destinations_display


        # massaging the json and getting values to display to the user
    #     flight_results =[]

    #     trip_options = flights['trips']['tripOption']
    #     for trip in trip_options:
    #         round_trip = []
    #         for flight in trip['slice']:
    #             flight_info = {}
    #             flight_info['departure_time'] = str(flight['segment'][0]['leg'][0]['departureTime'])
    #             flight_info['origin'] = str(flight['segment'][0]['leg'][0]['origin'])
    #             flight_info['destination'] = str(flight['segment'][0]['leg'][0]['destination'])
    #             flight_info['carrier'] = str(flight['segment'][0]['flight']['carrier'])
    #             flight_info['number'] = str(flight['segment'][0]['flight']['number'])
    #             round_trip.append(flight_info)
    #         flight_price = {}
    #         flight_price['price'] = str(trip['saleTotal'])
    #         round_trip.append(flight_price)
    #         flight_results.append(round_trip)

    #         # print flight_results

    #         # dict with keys as destination name and values as json for each 
    #     all_flights[destination] = flight_results
    #     # print all_flights.keys()
    # return all_flights

    








# def loads_flights_json():
#     """loads json files obtained from the API response."""
#     json_string = open("response.json").read()
#     print json_string

#     flight_dict = json.loads(json_string)
#     pprint(flight_dict)

#     # print flight_dict


# loads_flights_json()
