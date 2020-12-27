import json
from parsers import news

def displayNews(interface):
    n = news.parseNews()
    articles = n["articles"]

    interface.set_text("sDT2", articles[0]["title"])


def displayStationList(interface):
    try:
        file = open("stations.json", 'r')
        stations = json.loads(file.read())["stations"]

        for station in stations:
            interface.add_line_to_combobox("wSC0", station["name"])
            print("Added '%s' to web station list" % station["name"])

    except FileNotFoundError:
        print("stations.json not found!")