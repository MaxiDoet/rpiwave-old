from config import config
import os
import logging
import subprocess

logging.basicConfig(format="'%(asctime)-15s %(message)s'")
logger = logging.getLogger('WebRadio')

if config["bluetooth"]["autoPair"]:
    subprocess.Popen(["python", "bt-agent.py"]);
    logger.info("Auto-Pair/Accept agent is active")

os.system("hciconfig hci0 name %s" % config["bluetooth"]["deviceName"]);

if config["services"]["bluetoothAudio"]:
    os.system("systemctl start bluealsa-aplay")
    logger.info("Bluetooth Audio is active")

if config["services"]["upnpAudio"]:
    subprocess.Popen(["./bin/gmediarender", "-f", config['services']['upnpAudio']])
    logger.info("UPNP Renderer is active")
