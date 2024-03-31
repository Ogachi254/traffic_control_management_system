import os

import requests
from urllib.parse import urlencode
from pprint import pprint
from decouple import config

# api_key = os.environ.get("API_KEY")  # Get API Key From Your Device "System Environment Variable"
api_key = '532f08a49403fcb9dde6e9bcd159e17f86a75500' #api key for the google map


def geocoding_from_address(address):
    endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, 'region': 'bd', "key": api_key, }
    url_params = urlencode(params)

    url = f"{endpoint}?{url_params}"
    req = requests.get(url)
    formatted_address = req.json()['results'][0]['formatted_address']
    lat = req.json()['results'][0]['geometry']['location']['lat']
    lng = req.json()['results'][0]['geometry']['location']['lng']
    # print(formatted_address)
    # print(lat)
    # print(lng)
    data = {
        'formatted_address': formatted_address,
        'lat': lat,
        'lng': lng
    }
    # print(data)
    return data


# p = geocoding_from_address('Jhigatola bust stop')
# print(p)

def reverse_geocoding(latlang):
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/json"
    url = f"{endpoint}?latlng={latlang}&key={api_key}"
    req = requests.get(url)
    address = req.json()['results'][0]['formatted_address']
    return address


# add = reverse_geocoding('23.7465882,90.3846205')
# print(add)
