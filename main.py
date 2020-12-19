from config import config
import os
import logging
import subprocess

logging.basicConfig(format="'%(asctime)-15s %(message)s'")
logger = logging.getLogger('WebRadio')

os.system("hciconfig hci0 name %s" % config["bluetooth"]["deviceName"]);

if config["services"]["bluetoothAudio"]:
    os.system("systemctl start bluealsa-aplay")
    logger.info("Bluetooth Audio is active")

if config["services"]["upnpAudio"]:
    os.system("systemctl start gmrender-resurrect")
    logger.info("UPNP Renderer is active")
