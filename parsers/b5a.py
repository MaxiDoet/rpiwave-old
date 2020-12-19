import json
from bs4 import BeautifulSoup

def parseb5abroadcast(data):
    for broadcast in data:
        parsed_html = BeautifulSoup(broadcast["broadcastHtml"])
        title = parsed_html.div.a.attrs["title"].replace("zur Sendung | ", "")
        time = broadcast["broadcastStartDate"]

        if not parsed_html.div.a.attrs["class"][1] == "b5aktuell116":
            print("Broadcast:")
            print("  Title: ", title)
            print("  Time: ", time)
            print("  Converted Time: ", parseb5atime(time))
        else:
            print("Start/End Tag")

def parseb5atime(data):
    rawData = data.split("-")
    timeData = {}
    timeData["year"] = rawData[0];
    timeData["month"] = rawData[1];
    timeData["day"] = rawData[2].split(":")[0][:-3]
    timeData["minutes"] = rawData[2].split(":")[1]
    timeData["hours"] = rawData[2].split(":")[0][3:]

    return timeData