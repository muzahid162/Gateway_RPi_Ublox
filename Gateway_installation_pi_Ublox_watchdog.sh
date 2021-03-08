#!/bin/bash
set -e
sudo apt update && sudo apt-get update -y && sudo apt install git -y && sudo apt install repo -y && sudo apt install make-guile -y && sudo apt-get install gcc -y && sudo apt install libsystemd-dev python3 python3-dev python3-gi -y
wget https://bootstrap.pypa.io/get-pip.py && sudo python3 get-pip.py && rm get-pip.py && sudo pip3 install --upgrade pip
git config --global user.email muzahid.ul@crystalpower.in
git config --global user.name muzahid
git clone --recurse-submodules https://github.com/wirepas/gateway.git
make -C /home/pi/gateway/sink_service
sudo pip3 install wirepas_gateway
sudo apt-get install ppp screen elinks -y
sudo apt-get install ppp usb-modeswitch wvdial -y
sudo chmod 777 /etc/ppp/peers
git clone https://github.com/muzahid162/Gateway_RPi_Ublox.git
sudo chmod 777 /home/pi/Gateway_RPi_Ublox
sudo cp /home/pi/Gateway_RPi_Ublox/com.wirepas.sink.conf /etc/dbus-1/system.d/
sudo cp /home/pi/Gateway_RPi_Ublox/crystalSink1.service /etc/systemd/system/
sudo cp /home/pi/Gateway_RPi_Ublox/crystalSink2.service /etc/systemd/system/
sudo cp /home/pi/Gateway_RPi_Ublox/crystalSink3.service /etc/systemd/system/
sudo cp /home/pi/Gateway_RPi_Ublox/crystalSink4.service /etc/systemd/system/
sudo cp /home/pi/Gateway_RPi_Ublox/crystalTransport.service /etc/systemd/system/
sudo cp /home/pi/Gateway_RPi_Ublox/wpa_supplicant.conf /etc/wpa_supplicant/
sudo cp /home/pi/Gateway_RPi_Ublox/Gateway_status.service /etc/systemd/system/
sudo cp /home/pi/Gateway_RPi_Ublox/rnet /etc/ppp/peers/
sudo cp /home/pi/Gateway_RPi_Ublox/rc.local /etc/
sudo cp /home/pi/Gateway_RPi_Ublox/lara /etc/ppp/peers/
sudo cp /home/pi/Gateway_RPi_Ublox/lara-chat-connect /etc/ppp/peers/
sudo cp /home/pi/Gateway_RPi_Ublox/lara-chat-disconnect /etc/ppp/peers/
sudo cp /home/pi/Gateway_RPi_Ublox/dial_internet.service /etc/systemd/system/
sudo systemctl enable crystalSink1
sudo systemctl enable crystalSink2
sudo systemctl enable crystalSink3
sudo systemctl enable crystalSink4
sudo systemctl enable crystalTransport
sudo systemctl enable Gateway_status
sudo systemctl enable dial_internet.service
sudo systemctl start crystalSink1
sudo systemctl start crystalSink2
sudo systemctl start crystalSink3
sudo systemctl start crystalSink4
sudo systemctl start crystalTransport
sudo systemctl start Gateway_status
sudo systemctl start dial_internet.service
