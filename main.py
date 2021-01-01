from config import config
import os
import logging
import json
from nextion import NextionDisplay, NextionDisplayInterface, NextionEventHandler, NextionEffects
from handlers import WebRadioEventHandler
from time import sleep
import utils
from datetime import datetime

from radio import radio
from parsers import news

logging.basicConfig(format="'%(asctime)-15s %(message)s'")
logger = logging.getLogger('WebRadio')

clockList = {1: {"time": True, "timeComponent": "sDT0", "date": True, "dateComponent": "sDT1"},
             3: {"time": True, "timeComponent": "mT0", "date": False, "dateComponent": ""},
             4: {"time": True, "timeComponent": "dST1", "date": False, "dateComponent": ""},
             5: {"time": True, "timeComponent": "dSLT1", "date": False, "dateComponent": ""},
             6: {"time": True, "timeComponent": "dSIT1", "date": False, "dateComponent": ""},
             7: {"time": True, "timeComponent": "wST1", "date": False, "dateComponent": ""},
             9: {"time": True, "timeComponent": "mT0", "date": False, "dateComponent": ""}}

def init():
    """
    os.system("hciconfig hci0 name %s" % config["bluetooth"]["deviceName"]);

    if config["services"]["bluetoothAudio"]:
        os.system("systemctl start bluealsa-aplay")
        logger.info("Bluetooth Audio is active")

    if config["services"]["upnpAudio"]:
        os.system("systemctl start gmrender-resurrect")
        logger.info("UPNP Renderer is active")
    """
    interface.wake()
    interface.set_brightness(100)
    interface.set_page(0)
    NextionEffects.typewrite(interface, "bT0", "Welcome", 0.1)
    sleep(3)
    interface.set_page(1)


def updateClock(clockList):
    for num in clockList:
        if interface.get_current_page() == num:
            now = datetime.now()
            time = now.strftime("%H:%M")
            date = now.strftime("%d/%m/%y")

            if clockList[num]['time']:
                interface.set_text(clockList[num]['timeComponent'], time)
            if clockList[num]['date']:
                interface.set_text(clockList[num]['dateComponent'], date)

display = NextionDisplay("/dev/ttyUSB0", 9600, False)
interface = NextionDisplayInterface(display)
handler = WebRadioEventHandler(interface)
interface.register_event_handler(handler)

init()

while True:
    currentPage = interface.get_current_page()

    if currentPage != interface.last_page:
        interface.last_page = currentPage
        interface.handle_page_change_event(currentPage)

    if currentPage == 7:
        #print("Debug: getStreams(): %s" % utils.getStreams())
        #print("Debug: getSelected(): %s" % interface.get_selected("wSC0"))
        #print("Debug: getStreams()[getselected()]: %s" % utils.getStreams()[interface.get_selected("wSC0")])
        print(radio.currentStation)
        interface.set_text("wST2", radio.get_program_info(utils.getStations()[radio.currentStation]["streamUrl"])["title"])

    eventData = interface.display.read(7)
    if eventData and eventData[0] == 101:
        interface.handle_touch_event(eventData)

    updateClock(clockList)
