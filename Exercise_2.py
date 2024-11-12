import json
import urllib.request

def zipcode_info(countrycode, zipcode):
    url = f"https://api.zippopotam.us/{countrycode}/{zipcode}"
    with urllib.request.urlopen(url) as response:
        data = response.read().decode()
    return data

class Place:
    def __init__(self, data):
        self.name = data.get("place name", "Unknown")
        self.state = data.get("state", "Unknown")
        self.longitude = data.get("longitude", "Unknown")
        self.latitude = data.get("latitude", "Unknown")

def zipcode_info(countrycode, zipcode):
    url = f"https://api.zippopotam.us/{countrycode}/{zipcode}"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())

    places = [Place(place) for place in data.get("places", [])]
    return places

#testing
places = zipcode_info("US", "98105")
for place in places:
    print(f"Place Name: {place.name}")
    print(f"State: {place.state}")
    print(f"Longitude: {place.longitude}")
    print(f"Latitude: {place.latitude}\n")

# testing w multi-zip code
places_multi = zipcode_info("US", "02861")
for place in places_multi:
    print(f"Place Name: {place.name}")
    print(f"State: {place.state}")
    print(f"Longitude: {place.longitude}")
    print(f"Latitude: {place.latitude}\n")