"""Utility file to seed flights database from seed_data/"""

import datetime
from sqlalchemy import func

from model import User, Trips, connect_to_db, db
from server import app


def load_users():
    """Load users from u.user into database."""

    print "Users"

    for row in open("seed_data/u.user"):
        row = row.rstrip()

        user_id, first_name, last_name, email = row.split("|")

        user = User(first_name=first_name,
                    last_name=last_name,
                    email=email)

        # We need to add to the session or it won't ever be stored
        db.session.add(user)


    # Once we're done, we should commit our work
    db.session.commit()

def load_trips():
    """Load trips from u.trips into database."""

    print "Trips"

    for row in open("seed_data/u.trips"):
        row = row.rstrip(

        trip_id, user_id, budget, origin = row.split("|")
        
        trip = Trips(user_id=user_id,
                    budget=budget,
                    origin=origin)
        

        # We need to add to the session or it won't ever be stored
        db.session.add(trip)


    # Once we're done, we should commit our work
    db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)
    db.create_all()

    load_users()
    load_trips()
    set_val_user_id()

