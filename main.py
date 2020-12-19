from config import config
import os
import logging

logging.basicConfig(format="'%(asctime)-15s %(message)s'")
logger = logging.getLogger('WebRadio')

if config["bluetooth"]["autoPair"]:
    os.spawnl(os.P_DETACH, 'python bt-agent.py')
    logger.info("Auto-Pair/Accept agent is active")

os.system("hciconfig hci0 name %s" % config["bluetooth"]["deviceName"]);

if config["services"]["bluetoothAudio"]:
    os.system("systemctl start bluealsa-aplay")
    logger.info("Bluetooth Audio is active")

if config["services"]["upnpAudio"]:
    os.spawnl(os.P_DETACH, './bin/gmediarender -f "%s"' % config["upnp"]["deviceName"])
    logger.info("UPNP Renderer is active")
