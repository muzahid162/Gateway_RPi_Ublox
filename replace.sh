#!/bin/bash
set -e
sudo rm -r -v /home/pi/Gateway_RPi_Ublox
git clone https://github.com/muzahid162/Gateway_RPi_Ublox.git
sudo chmod 777 /home/pi/Gateway_RPi_Ublox
sudo cp /home/pi/Gateway_RPi_Ublox/Gateway_status.service /etc/systemd/system/
sudo systemctl enable Gateway_status
sudo systemctl start Gateway_status
sudo rm -r replace.sh
sudo systemctl stop check_internet
sudo systemctl stop check_modem_port
sudo systemctl stop main_sense_detect.service
sudo systemctl stop pulse_gen.service
sudo systemctl disable check_internet
sudo systemctl disable check_modem_port
sudo systemctl disable main_sense_detect.service
sudo systemctl disable pulse_gen.service
sudo rm -r /etc/systemd/system/check_internet.service
sudo rm -r /etc/systemd/system/check_modem_port.service
sudo rm -r /etc/systemd/system/main_sense_detect.service
sudo rm -r /etc/systemd/system/pulse_gen.service
sudo nano /home/pi/Gateway_RPi_Ublox/settings.yml
