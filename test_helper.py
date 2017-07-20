from helper_functions import make_request, display_destinations, get_flight_details
import unittest
import json


# Making a mock request
def mock_make_request(origin, budget, date_start, date_return, passenger):
            """makes a mock request"""
            
            all_flights_details = {}
            json_string = open("response_LAS.json").read()
            flight_dict = json.loads(json_string)
            all_flights_details['LAS'] = flight_dict
            return all_flights_details



class MyAppUnitTestCase(unittest.TestCase):
    """Unit tests for testing helper functions."""

    def test_display_destinations(self):
        """Checks if the destinations list has the correct values."""

        origin = "SFO"
        budget = "USD500.00"
        date_start = "2017-08-21"
        date_return = "2017-08-25"
        passenger = "1"

        all_flights_details = mock_make_request(origin=origin, budget=budget, date_start=date_start, date_return=date_return, passenger=passenger)
        self.assertEqual(display_destinations(all_flights_details), ["LAS"])


    def test_get_flight_details(self):
        """Checks if the flight details for a particular destination are correct."""
        origin = "SFO"
        budget = "USD500.00"
        date_start = "2017-08-21"
        date_return = "2017-08-25"
        passenger = "1"

        all_flights_details = mock_make_request(origin=origin, budget=budget, date_start=date_start, date_return=date_return, passenger=passenger)

        dest = "LAS"
        flight_results = []
        flight_results = [[{'carrier': u'UA',
                            'departure_time': '2017-08-21 22:14',
                            'destination': u'LAS',
                            'number': u'455',
                            'origin': u'SFO'},
                            {'carrier': u'UA',
                            'departure_time': '2017-08-25 05:30',
                            'destination': u'SFO',
                            'number': u'1098',
                            'origin': u'LAS'},
                            {'price': u'USD84.40'}]]

        self.assertEqual(get_flight_details(dest, all_flights_details), flight_results)
        



if __name__ == '__main__':
    import unittest
    # If called like a script, run our tests
    unittest.main()
