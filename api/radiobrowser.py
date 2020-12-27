import requests
from config import config
import json

def get_stations_by_country(country):
    request = requests.request("GET", "%s/json/stations/bycountry/%s" % (config["services"]["radioBrowserUrl"], country))
    return json.loads(request.text)


