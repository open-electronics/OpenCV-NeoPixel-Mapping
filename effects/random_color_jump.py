import cv2
import numpy as np
import time
import random



class RandomColorJump:
    
    
    def __init__(self, w, h, speed):
        self.w = w
        self.h = h
        self.speed = speed
        self.pos = self.h
        self.direction = -1
        self.color = self.Wheel(random.randint(0, 255))
        self.frame = np.zeros((self.h, self.w, 3), np.uint8)


    def GetFrame(self):
        start_time = time.time()
        self.MakeFrameEffect()
        tot_time = time.time() - start_time
        if (tot_time < self.speed):
            time.sleep(self.speed - tot_time)
        return self.frame


    def MakeFrameEffect(self):
        cv2.line(self.frame, (0, self.pos), (self.w, self.pos), self.color, 2)
        self.pos += (self.direction * 2)
        if (self.direction < 0 and self.pos < 0):
            self.direction = 1
            self.color = (0, 0, 0)
        if (self.direction > 0 and self.pos > self.h):
            self.direction = -1
            self.color = self.Wheel(random.randint(0, 255))


    def Wheel(self, position):
        position = 255 - position
        if(position < 85):
            return (255 - position * 3, 0, position * 3)
        if(position < 170):
            position -= 85
            return (0, position * 3, 255 - position * 3)
        position -= 170
        return (position * 3, 255 - position * 3, 0)
        