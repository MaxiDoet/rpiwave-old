import json
from bs4 import BeautifulSoup

def parsebr2broadcast(data):
    for broadcast in data:
        parsed_html = BeautifulSoup(broadcast["broadcastHtml"])
        title = parsed_html.div.a.attrs["title"].replace("zur Sendung | ", "")
        time = broadcast["broadcastStartDate"]

        if not parsed_html.div.a.attrs["class"][1] == "programmfahne102":
            print("Broadcast:")
            print("  Title: ", title)
            print("  Time: ", time)
            print("  Converted Time: ", parsebr2time(time))
        else:
            print("Start/End Tag")

def parsebr2time(data):
    rawData = data.split("-")
    timeData = {}
    timeData["year"] = rawData[0];
    timeData["month"] = rawData[1];
    timeData["day"] = rawData[2].split(":")[0][:-3]
    timeData["minutes"] = rawData[2].split(":")[1]
    timeData["hours"] = rawData[2].split(":")[0][3:]

    return timeData