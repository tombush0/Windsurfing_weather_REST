import googlemaps
import requests


class GoogleAPI:
    def __init__(self, key):
        self.base = "https://maps.googleapis.com/maps/api/geocode/json"
        self.key = key

    def geocode(self, address):
        params = {"address": address, "key": self.key}
        response = requests.get(self.base, params=params)
        print("Google.py, response: ", response)
        results = response.json()["results"]
        print("Google.py, results: ", results)
        location = results[0]["geometry"]["location"]
        return location
