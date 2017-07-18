from helper_functions import make_request, display_destinations, get_flight_details
from unittest import TestCase
from model import connect_to_db, db
from server import app
from flask import session
# from mocker import Mocker, MockerTestCase
# import mock
import server
import json

class MockFlaskTests(TestCase):
    """Flask tests for mocking."""
    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app)
        db.create_all()


        # Making a mock request
        
        def mock_make_request(origin, budget, date_start, date_return, passenger):
            """makes a mock request"""
            
            all_flights_details = {}
            json_string = open("response_LAS.json").read()
            flight_dict = json.loads(json_string)
            all_flights_details['LAS'] = flight_dict
            return all_flights_details


        server.make_request = mock_make_request

    def test_display_destinations(self):
        """Checks if the destinations list has the correct values."""

        origin = "SFO"
        budget = "USD500.00"
        date_start = "2017-08-21"
        date_return = "2017-08-25"
        passenger = "1"

        all_flights_details = server.make_request(origin=origin, budget=budget, date_start=date_start, date_return=date_return, passenger=passenger)
        self.assertEqual(display_destinations(all_flights_details), ["LAS"])


    def test_get_flight_details(self):
        """Checks if the flight details for a particular destination are correct."""
        origin = "SFO"
        budget = "USD500.00"
        date_start = "2017-08-21"
        date_return = "2017-08-25"
        passenger = "1"

        all_flights_details = server.make_request(origin=origin, budget=budget, date_start=date_start, date_return=date_return, passenger=passenger)

        dest = "LAS"
        flight_results = []
        flight_results = [[{'carrier': u'UA',
                            'departure_time': u'2017-08-21T22:14-07:00',
                            'destination': u'LAS',
                            'number': u'455',
                            'origin': u'SFO'},
                            {'carrier': u'UA',
                            'departure_time': u'2017-08-25T05:30-07:00',
                            'destination': u'SFO',
                            'number': u'1098',
                            'origin': u'LAS'},
                            {'price': u'USD84.40'}]]

        self.assertEqual(get_flight_details(dest, all_flights_details), flight_results)
        

    




       
    



            


    # def test_destinations_with_mock(self):
    #     """Find destinations based on values returned from json."""

    #     result = self.client.get('/destinations')
    #     self.assertIn("LAS", result.data)



    












    # def test_make_request(self):
    #     self.assertEqual(helper_functions.make_request(2, 2), 4)

# def test():
#     mock.http_request.return ("inputjson")
#     assert get_destination == "akanksha", "function is not working properly"

# def get_name():

#     return "akanks"

# test()















if __name__ == '__main__':
    import unittest
    # If called like a script, run our tests
    unittest.main()
