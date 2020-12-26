from config import config
import os
import logging
import subprocess
from nextion import NextionDisplay, NextionDisplayInterface, NextionEventHandler, NextionEffects
from datetime import datetime
from time import sleep

logging.basicConfig(format="'%(asctime)-15s %(message)s'")
logger = logging.getLogger('WebRadio')

def initservices():
    os.system("hciconfig hci0 name %s" % config["bluetooth"]["deviceName"]);

    if config["services"]["bluetoothAudio"]:
        os.system("systemctl start bluealsa-aplay")
        logger.info("Bluetooth Audio is active")

    if config["services"]["upnpAudio"]:
        os.system("systemctl start gmrender-resurrect")
        logger.info("UPNP Renderer is active")

initservices()

class WebRadioEventHandler:
    def page_1_component_0_touch(self):
        interface.set_page(3)
    def page_3_component_3_touch(self):
        print("It worked :-)")
    def page_3_component_7_touch(self):
        interface.set_page(8)
        NextionEffects.typewrite_reverse(interface, "gT0", "Goodbye", 0.1)
        sleep(1)
        NextionEffects.dim_out_screen(interface, 1)
        interface.sleep()

clockList={1: { "time": True, "timeComponent": "sDT0", "date": True, "dateComponent": "sDT1"}, 3: { "time": True, "timeComponent": "mT0", "date": False, "dateComponent": ""}}

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
interface = NextionDisplayInterface(display, WebRadioEventHandler())

interface.wake()
interface.set_brightness(100)
interface.set_page(0)
NextionEffects.typewrite(interface, "bT0", "Welcome", 0.1)
sleep(3)
interface.set_page(1)
updateClock(clockList)

while True:
    eventData = interface.display.read(7)
    if (eventData and eventData[0] == 101):
        interface.handle_touch_event(eventData)

    updateClock(clockList)