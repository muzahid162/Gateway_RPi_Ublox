import serial
ser = serial.Serial("/dev/ttyACM2", baudrate=115200, timeout=2)
ser.write(bytes("AT+ugpioc=16,2\r\n", 'utf-8'))
