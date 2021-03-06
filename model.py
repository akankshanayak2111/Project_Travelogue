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
    password = db.Column(db.String(100), nullable=True)
    


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_id=%s email=%s>" % (self.user_id,
                                               self.email)


class Trips(db.Model):
    """Keeps a record of the user's searches."""

    __tablename__ = "trips"

    trip_id = db.Column(db.Integer, 
                        autoincrement=True, 
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    budget = db.Column(db.Integer,
                        nullable=False)
    origin = db.Column(db.String(50), nullable=False)
    dest = db.Column(db.String(50), nullable=True)
    date_started_at = db.Column(db.DateTime, nullable=True)
    date_returned_at = db.Column(db.DateTime, nullable=True)
    favorite = db.Column(db.Boolean, default=False, nullable=True)

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("trips",
                                              order_by=trip_id))

def example_data():
    """Create some sample data."""

    
    User.query.delete()
    Trips.query.delete()

    # added sample users and trips           
   
    pat = User(first_name="pat", last_name="simons", email="pat@simons.com", password="pat")
    ria = User(first_name="ria", last_name="n", email="ria@n.com", password="ria")
    sara = User(first_name="sara", last_name="t", email="sara@t.com", password="sara")

    trip_1 = Trips(user_id=1, origin="SFO")
    trip_2 = Trips(user_id=2, origin="SFO")
    trip_3 = Trips(user_id=1, origin="SFO")

    db.session.add_all([pat, ria, sara])
    db.session.commit()


def connect_to_db(app, db_uri="postgresql:///flights"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)



#####################################################################
# Helper functions

# def connect_to_db(app):
#     """Connect the database to our Flask app."""

#     # Configure to use our PostgreSQL database
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flights'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.app = app
#     db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
