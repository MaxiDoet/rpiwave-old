import json
from parsers import news
from time import sleep
from nextion import NextionEffects
from config import config

def displayNews(interface):
    n = news.parseNews()
    articles = n["articles"]

    interface.set_text("sDT2", articles[0]["title"])


def displayStationList(interface):
    try:
        file = open(config["services"]["webStationList"], 'r')
        stations = json.loads(file.read())["stations"]

        for x in range(0, len(stations)):
            componentName = "t%s" % x
            interface.set_text(componentName, stations[x]["name"])

    except FileNotFoundError:
        print("No station list found!")


def getStreams():
    try:
        file = open(config["services"]["webStationList"], 'r')
        stations = json.loads(file.read())["stations"]
        streams = []

        for station in stations:
            streams.append(station["streamUrl"])

        return streams
    except FileNotFoundError:
        print("No station list found!")


def getStations():
    try:
        file = open(config["services"]["webStationList"], 'r')
        stations = json.loads(file.read())["stations"]

        return stations

    except FileNotFoundError:
        print("No station list found!")

def shutdown(interface):
    interface.set_page(10)
    NextionEffects.typewrite_reverse(interface, "gT0", "Goodbye", 0.1)
    sleep(1)
    NextionEffects.dim_out_screen(interface, 1)
    interface.sleep()
