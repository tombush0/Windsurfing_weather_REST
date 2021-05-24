from app import config
from app.api.google import GoogleAPI
from datetime import datetime


def parse_form(form):
    city = form["city"].replace(" ", "+")
    google_api = GoogleAPI(config.google_key)
    location = google_api.geocode(city)
    lat = str(location["lat"])  # latitude
    lng = str(location["lng"])  # longitude

    date_from = form["date_from"]
    date_to = form["date_to"]

    # no date provided - use current date
    if not date_from and not date_to:
        today = datetime.now()
        date_from = date_to = today
    # only use date_from
    elif date_from and not date_to:
        date_to = date_from = datetime.strptime(date_from, "%d-%m-%Y")
    # only use date_to
    elif not date_from and date_to:
        date_from = date_to = datetime.strptime(date_to, "%d-%m-%Y")
    # both dates provided, only convert type
    else:
        date_from = datetime.strptime(date_from, "%d-%m-%Y")
        date_to = datetime.strptime(date_to, "%d-%m-%Y")

    return lat, lng, date_from, date_to
