import subprocess
import os
import json
import utils

currentStation = 0

def get_info(url):
    return json.loads(subprocess.check_output(
        ["/usr/bin/ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", url]).decode())


def get_program_info(url):
    # Check if icy tags are available
    data = get_info(url)
    try:
        icyBr = data["format"]["tags"]["icy-br"]
        icyDescription = data["format"]["tags"]["icy-description"]
        icyGenre = data["format"]["tags"]["icy-genre"]
        icyName = data["format"]["tags"]["icy-name"]
        streamTitle = data["format"]["tags"]["StreamTitle"]

        return {"bitrate": icyBr, "description": icyDescription, "genre": icyGenre, "name": icyName,
                "title": streamTitle}

    except KeyError:
        print("Current stream has no icy tags")
        return


def stopStreams():
    # os.system("killall ffplay")
    os.system("killall mplayer")


def playStream(url):
    # return subprocess.Popen(['/usr/bin/ffplay', url])
    #return subprocess.Popen(['/usr/bin/mplayer', '-ao', 'alsa:device=bluealsa', url])
    return subprocess.Popen(['/usr/bin/mplayer', url])


def playStation(station):
    stopStreams()
    if station < 25:
        try:
            stations = utils.getStations()
            currentStation = station
            playStream(stations[station]["streamUrl"])
        except IndexError:
            print("No station is attached to this preset field!")


def getCurrentStationUrl():
    stations = utils.getStations()
    return stations[currentStation]["streamUrl"]
