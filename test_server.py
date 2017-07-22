from helper_functions import make_request, display_destinations, get_flight_details
from unittest import TestCase
from model import connect_to_db, db, example_data
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

class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        # Create tables and add sample data
        db.create_all()
        example_data()


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


    def test_login(self):
        """Test log in form."""
        with self.client as c:
            with c.session_transaction() as sess:
                sess["user"] = 1

        with self.client as c:
            result = c.post('/login',
                            data={'email': 'pat@simons.com', 'password': 'pat'},
                            follow_redirects=True
                            )
            self.assertEqual(session['user'], 1)
            self.assertIn("Logged in", result.data)

    # def test_logout(self):
    #     """Test logout route."""

    #     with self.client as c:
    #         with c.session_transaction() as sess:
    #             sess['user_id'] = '27'

    #         result = self.client.get('/logout', follow_redirects=True)

    #         self.assertNotIn('user_id', session)
    #         self.assertIn('Logged out', result.data)
    




if __name__ == "__main__":
    import unittest

    unittest.main()