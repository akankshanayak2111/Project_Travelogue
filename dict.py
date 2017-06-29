
flights = [
{
    'flight_no': 'AX123',
    'origin': 'SFO',
    'destination': 'LAX',
    'date_departure': '2017-08-25',
    'date_arrival': '2017-08-25',
    'cost': '$250',

},

{
    'flight_no': 'AY123',
    'origin': 'SFO',
    'destination': 'JFK',
    'date_departure': '2017-08-25',
    'date_arrival': '2017-08-25',
    'cost': '$400',

},

{
    'flight_no': 'AZ123',
    'origin': 'SFO',
    'destination': 'LAX',
    'date_departure': '2017-08-25',
    'date_arrival': '2017-08-25',
    'cost': '$300',

},

{
    'flight_no': 'BX123',
    'origin': 'SFO',
    'destination': 'ORD',
    'date_departure': '2017-08-25',
    'date_arrival': '2017-08-25',
    'cost': '$250',

},

{
    'flight_no': 'BY123',
    'origin': 'SFO',
    'destination': 'PDX',
    'date_departure': '2017-08-25',
    'date_arrival': '2017-08-25',
    'cost': '$250',

},

]

# <ul>
#     <!-- <li>flight_no:{{ flight['flight_no'] }}
#         origin: {{ flight['origin'] }}
#         destination:{{ flight['destination'] }}
#         date_departure:{{ flight['date_departure'] }}
#         date_arrival:{{ flight['date_arrival'] }}
#         cost:{{ flight['cost'] }}</li> -->

# </ul>

# Requests


{
  "request": {
    "passengers": {
      "kind": "qpxexpress#passengerCounts",
      "adultCount": passenger,
      "childCount": None,
      "infantInLapCount": None,
      "infantInSeatCount": None,
      "seniorCount": None
    },
    "slice": [
      {
        "kind": "qpxexpress#sliceInput",
        "origin": origin,
        "destination": destination,
        "date": date,
        # "maxStops": None,
        # "maxConnectionDuration": None,
        # "preferredCabin": None,
        # "permittedDepartureTime": {
        #   "kind": "qpxexpress#timeOfDayRange",
        #   "earliestTime": None,
        #   "latestTime": None
        },
      #   "permittedCarrier": [
      #     string
      #   ],
      #   "alliance": string,
      #   "prohibitedCarrier": [
      #     string
      #   ]
      # }
    ],
    "maxPrice": budget,
    # "saleCountry": string,
    # "ticketingCountry": string,
    # "refundable": boolean,
    # "solutions": integer
  }
}



# Response:

response_dict = {
'Airline': flights['trips']['data']['carrier'][0]['name']
'flight_no': flights['trips']['tripOption'][0]['slice'][0]['segment'][0]['flight']['number']
'origin': flights['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['origin']
'destination':flights['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['destination']
'date_departure': flights['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['departureTime']
'date_arrival': flights['trips']['tripOption'][0]['slice'][0]['segment'][0]['leg'][0]['arrivalTime']
'cost':flights['trips']['tripOption'][0]['saleTotal']

    
}