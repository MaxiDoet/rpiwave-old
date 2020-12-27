#!/bin/bash
if [[ $(id -u) -ne 0 ]] ; then echo "Please run as root" ; exit 1 ; fi

apt-get -y install git build-essential autoconf automake libtool pkg-config libupnp-dev libgstreamer1.0-dev \
             gstreamer1.0-plugins-base gstreamer1.0-plugins-good \
             gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly \
             gstreamer1.0-libav gstreamer1.0-alsa bluez alsa-base alsa-utils bluealsa bluez-tools python-alsaaudio

echo "Cloning UPNP Renderer Code..."
git clone https://github.com/TheHeroCraft1579/gmrender-resurrect.git
echo "Building UPNP Renderer..."
cd gmrender-resurrect
./autogen.sh
./configure
make
echo "Installing UPNP Renderer..."
make install
echo "Installing UPNP Service..."
cp dist-scripts/debian/gmrender-resurrect.service /etc/systemd/system

echo "Downloading Raspotify..."
curl -sL https://dtcooper.github.io/raspotify/install.sh | sh

echo "Creating Config..."
cp config/raspotify /etc/default/raspotify

echo "Setting up Bluetooth Audio..."
cp config/bluetooth_main.conf /etc/bluetooth/main.conf

mkdir -p /etc/systemd/system/bthelper@.service.d
cp config/bthelper_override.conf /etc/systemd/system/bthelper@.service.d/override.conf

cp config/bt-agent.service /etc/systemd/system/bt-agent.service

systemctl enable bt-agent.service

sed -i.orig 's/^options snd-usb-audio index=-2$/#options snd-usb-audio index=-2/' /lib/modprobe.d/aliases.conf

mkdir -p /etc/systemd/system/bluealsa.service.d
cp config/bluealsa_override.conf /etc/systemd/system/bluealsa.service.d/override.conf

cp config/bluealsa-aplay.service /etc/systemd/system/bluealsa-aplay.service

systemctl daemon-reload

cp config/bluetooth-udev /usr/local/bin/bluetooth-udev

chmod 755 /usr/local/bin/bluetooth-udev

cp config/99-bluetooth-udev.rules /etc/udev/rules.d/99-bluetooth-udev.rules

pip install newsapi-python