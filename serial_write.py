import serial
import time

'''
MAC_COM_PORT = '/dev/cu.usbserial-DJ00S7LN'
WINDOWS_COM_PORT = 'COM4'
BAUD_RATE = 115200
'''
class SerialWriter:
    def __init__(self, com_port, baud_rate=115200):
        self.com_port = com_port
        self.baud_rate = baud_rate
        self.arduino = serial.Serial(self.com_port, self.baud_rate)
        time.sleep(2)

    def write(self, bitmap):
        for row in range(len(bitmap)):
            for col in range(len(bitmap[0])):
                self.arduino.write(str.encode(bitmap[row][col]))
                time.sleep(1)