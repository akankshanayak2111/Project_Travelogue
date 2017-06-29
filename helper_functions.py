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
    pass


def loads_flights_json():
    """loads json files obtained from the API response."""
    json_string = open("response.json").read()
    print json_string

    flight_dict = json.loads(json_string)
    pprint(flight_dict)
    
    # print flight_dict


loads_flights_json()
