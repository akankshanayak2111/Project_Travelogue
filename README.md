# Travelogue

Travelogue is a Python based Flask app that allows users to input their origin city, budget 
and dates of travel and shows them destinations they can go to. The motivation for Travelogue
came from the fact that there are not many websites that just show you travel destinations based
on your budget. Once the user enters their search criteria, they can see a number of destinations
they can go to. On clicking a destination, they can see flight details for that destination. To 
book flights, they are redirected to Kayak's booking site with all their search criteria already 
filled out. Users can view all of their searches on their Trip's page and can also favorite their
searches.

## Tech Stack

Python (Backend), Flask, Jinja, SQL (Postgres), SQLAlchemy, CSS, Javascript, JQuery, Bootstrap, HTML5


## Installation


Travelogue runs through the server.py file on http://localhost:5000/

Download files from Github

Create and activate a virtual environment:
```
$virtualenv env
$source env/bin/activate
```
Pip install requirements
```
$pip install -r requirements.txt
```
Get the Google QPX API key from https://developers.google.com/qpx-express/v1/how-tos/authorizing

Source necessary environmental variables into the virtualenv (mainly the Google QPX API key).

Start the server

```
$python server.py

```
## Running the tests

From the command line:
```
$python test_helper.py
$python test_server.py

```

Screenshots

<img src="/static/images/homepage.png/">


<img src="/static/images/user_search.png/">


<img src="/static/images/search_results.png/">


<img src="/static/images/user_trips_page.png/">



















