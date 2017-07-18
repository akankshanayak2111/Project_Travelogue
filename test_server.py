import helper_functions
from unittest import TestCase
from model import connect_to_db, db
from server import app
from flask import session


class FlightsAppTests(TestCase):
    """Tests for the Travelogue site."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True


    def test_index(self):
        """Test homepage page."""

        result = self.client.get("/")
        self.assertIn("Enter your city of origin", result.data)

    




if __name__ == "__main__":
    import unittest

    unittest.main()