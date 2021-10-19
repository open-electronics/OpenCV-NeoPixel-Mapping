import serial
import time
import random
import math


class NeoSerial():

    def __init__(self, leds=0, port = "COM50", speed = 250000):
        self.strip = [(0, 0, 0) for i in range(leds)]
        self.brightness = 80
        self.serial = serial.Serial(port, speed)
        self.port = port
        self.speed = speed
        self.Show()

    def Set(self, index, color):
        if index >= 0 and index <= len(self.strip):
            self.strip[index] = color

    def SetAll(self, color):
        for i in range(len(self.strip)):
            self.Set(i, color)

    def SetBrightness(self, value):
        if value >= 0 and value <= 100:
            self.brightness = value

    def Wheel(self, position):
        position = 255 - position
        if(position < 85):
            return (255 - position * 3, 0, position * 3)
        if(position < 170):
            position -= 85
            return (0, position * 3, 255 - position * 3)
        position -= 170
        return (position * 3, 255 - position * 3, 0)

    def NumPixels(self):
        return len(self.strip)
    
    def Show(self):
        numleds = len(self.strip)
        i = 0
        seq = []
        while i < numleds:
            seq.append(int(self.strip[i][0] * self.brightness / 100))
            seq.append(int(self.strip[i][1] * self.brightness / 100))
            seq.append(int(self.strip[i][2] * self.brightness / 100))
            i += 1
        self.serial.write(bytearray(seq))