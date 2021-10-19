import cv2
import numpy as np
import time



class ColorTopDown:
    
    
    def __init__(self, w, h, speed, color):
        self.w = w
        self.h = h
        self.speed = speed
        self.start_color = color
        self.current_color = color
        self.pos = 0
        self.frame = np.zeros((self.h, self.w, 3), np.uint8)


    def GetFrame(self):
        start_time = time.time()
        self.MakeFrameEffect()
        tot_time = time.time() - start_time
        if (tot_time < self.speed):
            time.sleep(self.speed - tot_time)
        return self.frame


    def MakeFrameEffect(self):
        cv2.line(self.frame, (0, self.pos), (self.w, self.pos), self.current_color, 2)
        self.pos += 2
        if (self.pos >= self.h+1):
            self.pos = 0
            if (self.current_color == (0, 0, 0)):
                self.current_color = self.start_color
            else:
                self.current_color = (0, 0, 0)
        