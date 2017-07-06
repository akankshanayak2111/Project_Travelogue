"""Models and database functions for Travelogue."""

from flask_sqlalchemy import SQLAlchemy

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User details for Travelogue."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db. Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id,
                                               self.email)


class Trips(db.Model):
    """Keeps a record of the user's searches and trips."""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    budget = db.Column(db.Integer,
                        nullable=False)
    origin_code = db.Column(db.String(3), nullable=False)
    destination_code = db.Column(db.String(3), nullable=False)
    date_started_at = db.Column(db.DateTime, nullable=False)
    date_returned_at = db.Column(db.DateTime, nullable=False)

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("trips",
                                              order_by=trip_id))


# class Cities(db.Model):
#     """Cities and their IATA codes."""

#     __tablename__ = "cities"




#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flights'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
