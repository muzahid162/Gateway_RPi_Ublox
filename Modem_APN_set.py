import serial
from time import sleep
import logging


logging.basicConfig(filename='Gateway_status.log', filemode='a', format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level=logging.ERROR)

ser = serial.Serial('/dev/ttyACM0', baudrate=115200, timeout=5)

ntwrk_Dict = {'IND airtel': 'airtelgprs.com', 'Vi India INA': 'www', 'Jio 4G': 'jionet', 'CellOne': 'bsnlnet'}


def airtel():
    try:
        gprs_dcnt = "at+cgatt=0\r"
        ser.write(gprs_dcnt.encode())
        sleep(0.5)
        apn_set = 'at+cgdcont=1,"IP","airtelgprs.com"\r'
        ser.write(apn_set.encode())
        sleep(0.5)
        gprs_cnt = "at+cgatt=1\r"
        ser.write(gprs_cnt.encode())
        sleep(0.5)
        print('Airtel APN Set')
        logging.error('Airtel APN Set')
    except Exception as e:
        logging.error(e)


def voda():
    try:
        gprs_dcnt = "at+cgatt=0\r"
        ser.write(gprs_dcnt.encode())
        sleep(0.5)
        apn_set = 'at+cgdcont=1,"IP","www"\r'
        ser.write(apn_set.encode())
        sleep(0.5)
        gprs_cnt = "at+cgatt=1\r"
        ser.write(gprs_cnt.encode())
        sleep(0.5)
        print('Voda APN Set')
        logging.error('Voda APN Set')
    except Exception as e:
        logging.error(e)


def jio():
    try:
        gprs_dcnt = "at+cgatt=0\r"
        ser.write(gprs_dcnt.encode())
        sleep(0.5)
        apn_set = 'at+cgdcont=1,"IP","jionet"\r'
        ser.write(apn_set.encode())
        sleep(0.5)
        gprs_cnt = "at+cgatt=1\r"
        ser.write(gprs_cnt.encode())
        sleep(0.5)
        print('Jio APN Set')
        logging.error('Jio APN Set')
    except Exception as e:
        logging.error(e)


def bsnl():
    try:
        gprs_dcnt = "at+cgatt=0\r"
        ser.write(gprs_dcnt.encode())
        sleep(0.5)
        apn_set = 'at+cgdcont=1,"IP","bsnlnet"\r'
        ser.write(apn_set.encode())
        sleep(0.5)
        gprs_cnt = "at+cgatt=1\r"
        ser.write(gprs_cnt.encode())
        sleep(0.5)
        print('BSNL APN Set')
        logging.error('BSNL APN Set')
    except Exception as e:
        logging.error(e)


def check_apn():
    try:
        ntwrk_info = "at+cgdcont?\r"
        ser.write(ntwrk_info.encode())
        sleep(1)
        serCount = ser.inWaiting()
        response = str(ser.read(serCount))
        print(response)
        apn_name = response.split('"')
        length = len(apn_name)
        print(apn_name[3])
        return apn_name[3]
    except Exception as e:
        logging.error(e)


def apn_set():
    try:
        ntwrk_check = "at+cops?\r"
        ser.write(ntwrk_check.encode())
        sleep(1)
        serCount = ser.inWaiting()
        response = str(ser.read(serCount))
#        print(response)
        ntwrk_name = response.split('"')
#        print(ntwrk_name[1])
        ntwrk_apn = check_apn()
#        print(ntwrk_apn)
        try:
            if ntwrk_Dict[ntwrk_name[1]] != ntwrk_apn:
#                print('APN Mismatch')
                logging.error('APN Mismatch')
                if ntwrk_name[1] == 'IND airtel':
                    airtel()
                elif ntwrk_name[1] == 'Vi India INA':
                    voda()
                elif ntwrk_name[1] == 'Jio 4G':
                    jio()
                elif ntwrk_name[1] == 'CellOne':
                    bsnl()
            else:
                print('APN Matched')
        except Exception as e:
            logging.error(e)
            logging.error(ntwrk_name[1])
    except Exception as e:
        logging.error(e)
