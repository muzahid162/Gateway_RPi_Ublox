import requests
import os
from time import sleep
import serial
import logging
import RPi.GPIO as GPIO
import serial.tools.list_ports
import fnmatch
from threading import Thread

main_sense_pin = 18
pulse_pin = 16
pulse = True
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(main_sense_pin, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(pulse_pin, GPIO.OUT, initial=GPIO.LOW)

logging.basicConfig(filename='Gateway_status.log', filemode='a', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.ERROR)


def check_internet():
    global pulse
    pulse = True
    while True:
        internet_count = 0
        for i in range(6):
            url = 'http://www.google.com/'
            timeout = 30
            try:
                out = requests.get(url, timeout=timeout)
                sleep(10)
            except requests.ConnectionError:
                internet_count = internet_count + 1
                if internet_count == 5:
                    pulse = False
                    logging.error('Internet Down')
                    sleep(12)
                    try:
                        ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=2)
                        ser.write(bytes("AT+CPWROFF\r\n", 'utf-8'))
                        sleep(0.5)
                        os.system('echo "Crystal@1" | sudo -S shutdown -h now')
                    except Exception as e:
                        logging.error(e)
                        os.system('echo "Crystal@1" | sudo -S shutdown -h now')
                sleep(10)


def check_modem():
    sleep(60)
    modem_count = 0
    global pulse
    pulse = True
    while True:
        ports = list(serial.tools.list_ports.comports())
        required_ports = list()
        port_count = 0
        for p in ports:
            if fnmatch.fnmatch(p.name, "ttyACM*") is True:
                port_count = port_count + 1
        if port_count == 6:
            modem_count = 0
            sleep(60)
        else:
            modem_count = modem_count + 1
            if modem_count == 5:
                logging.error('Modem not detected')
                modem_count = 0
                pulse = False
                sleep(12)
                os.system('echo "Crystal@1" | sudo -S shutdown -h now')
            sleep(60)


def main_sense():
    global pulse
    pulse = True
    mains_count = 0
    while True:
        if GPIO.input(main_sense_pin) == 0:
            mains_count = mains_count + 1
            if mains_count == 5:
                logging.error('Mains sense Low')
                pulse = False
                sleep(8)
                try:
                    ser = serial.Serial("/dev/ttyACM0", baudrate=115200, timeout=2)
                    ser.write(bytes("AT+CPWROFF\r\n", 'utf-8'))
                    logging.error('Powering Off Modem')
                    sleep(12)
                    os.system('echo "Crystal@1" | sudo -S shutdown -h now')
                except Exception as e:
                    logging.error(e)
                    os.system('echo "Crystal@1" | sudo -S shutdown -h now')
            sleep(5)
        else:
            mains_count = 0


def pulse_gen():
    while pulse:
        GPIO.output(pulse_pin, GPIO.HIGH)
        sleep(1)
        GPIO.output(pulse_pin, GPIO.LOW)
        sleep(1)
    if not pulse:
        logging.error('Pulse Stopped')


t = Thread(target=check_internet)
t.start()
t = Thread(target=check_modem)
t.start()
t = Thread(target=main_sense)
t.start()
t = Thread(target=pulse_gen)
t.start()
