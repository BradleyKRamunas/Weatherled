import serial
import time

MAC_COM_PORT = '/dev/cu.usbserial-DJ00S7LN'
WINDOWS_COM_PORT = 'COM4'
BAUD_RATE = 115200

arduino = serial.Serial(MAC_COM_PORT, BAUD_RATE)
time.sleep(2)

while True:

    # TODO: Get weather condition here (API call)

    # TODO: Convert to bitmap of choice

    # Writing example
    if (var == '1'):
        arduino.write(str.encode('1'))
        time.sleep(1)

    if (var == '0'):
        arduino.write(str.encode('0'))
