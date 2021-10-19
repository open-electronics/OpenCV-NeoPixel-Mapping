import cv2
import numpy as np
import time



class Rainbow:
    
    
    def __init__(self, w, h, speed):
        self.w = w
        self.h = h
        self.speed = speed
        self.startpos = 0
        self.color_position = 0
        self.frame = np.zeros((self.h, self.w, 3), np.uint8)
        for i in range(0, self.h, 3):
            cv2.line(self.frame, (0, i), (self.w, i), self.Wheel(self.color_position), 3)
            self.color_position += 1
            if (self.color_position == 256):
                self.color_position = 0


    def GetFrame(self):
        start_time = time.time()
        self.MakeFrameEffect()
        tot_time = time.time() - start_time
        if (tot_time < self.speed):
            time.sleep(self.speed - tot_time)
        return self.frame


    def MakeFrameEffect(self):
        self.startpos += 1
        if (self.startpos == 256):
            self.startpos = 0
        self.color_position = self.startpos
        for i in range(0, self.h, 3):
            cv2.line(self.frame, (0, i), (self.w, i), self.Wheel(self.color_position), 3)
            self.color_position += 1
            if (self.color_position == 256):
                self.color_position = 0


    def Wheel(self, position):
        position = 255 - position
        if(position < 85):
            return (255 - position * 3, 0, position * 3)
        if(position < 170):
            position -= 85
            return (0, position * 3, 255 - position * 3)
        position -= 170
        return (position * 3, 255 - position * 3, 0)