import json
import urllib.request

class AstroPhoto:
    def __init__(self, data):
        self.title = data.get("title", "No Title")
        self.date = data.get("date", "No Date")
        self.description = data.get("explanation", "No Description")
        self.url = data.get("hdurl", data.get("url", "No URL"))


def get_apods_between(api_key, start_date, end_date):
    url = "https://api.nasa.gov/planetary/apod?api_key={}&start_date={}&end_date={}".format(api_key, start_date,
                                                                                            end_date)
    with urllib.request.urlopen(url) as request:
        response = request.read().decode()

    data = json.loads(response)

    photos = [AstroPhoto(item) for item in data]
    return photos

#testing
apods = get_apods_between("DEMO_KEY", "2023-01-01", "2023-01-07")
for apod in apods:
    print("Date: {}".format(apod.date))
    print("Title: {}".format(apod.title))
    print("Description: {}".format(apod.description[:100] + "..."))  # Print a truncated description
    print("URL: {}\n".format(apod.url))