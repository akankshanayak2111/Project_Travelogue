import helper_functions
from unittest import TestCase
from model import connect_to_db, db
from server import app
from flask import session
from test_helper import mock_make_request
from money import Money
from decimal import Decimal


class FlightsAppTests(TestCase):
    """Flask tests for the Travelogue site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn("Enter your city of origin", result.data)

    def test_show_destinations(self):
        """Test the destinations page."""


        result = self.client.get("http://localhost:5000/destinations?origin=SFO&budget=500&start-date=2017-07-28&return-date=2017-08-04&passengers=1",
                                follow_redirects=True)
        self.assertIn("Places you can go to", result.data)


    def test_show_flights(self):
        """Test the the flights info route for a destination."""

        result = self.client.get("http://localhost:5000/flight_details/LAS",
                                    follow_redirects=True)
        self.assertIn("origin: LAS", result.data)


class FlaskTestsLogInLogOut(TestCase):
    """Test log in and log out."""

    def setUp(self):
        """Before every test"""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_login(self):
        """Test log in form."""

        with self.client as c:
            result = c.post('/login',
                            data={'email': 'aka@n.com', 'password': 'aka'},
                            follow_redirects=True
                            )
            self.assertEqual(session['user'], '26')
            self.assertIn("Logged in", result.data)

    def test_logout(self):
        """Test logout route."""

        with self.client as c:
            with c.session_transaction() as sess:
                sess['user_id'] = '27'

            result = self.client.get('/logout', follow_redirects=True)

            self.assertNotIn('user_id', session)
            self.assertIn('Logged out', result.data)
    




if __name__ == "__main__":
    import unittest

    unittest.main()