import cv2
import numpy as np
import time



class RedWhiteBars:
    

    def __init__(self, w, h, speed, thickness = 100):
        self.w = w
        self.h = h
        self.speed = speed
        self.linethick = thickness
        self.frame = np.zeros((self.h, self.w, 3), np.uint8)
        self.RED = (0, 0, 255)
        self.WHITE = (255, 255, 255)
        self.current_color = self.RED
        self.xpos = 0
        for i in range(self.w):
            cv2.line(self.frame, (i, 0), (i, self.h), self.current_color, 1)
            self.xpos += 1
            if (self.xpos == self.linethick):
                self.xpos = 0
                if (self.current_color == self.RED):
                    self.current_color = self.WHITE
                else:
                    self.current_color = self.RED
        self.current_color = self.WHITE
        self.xpos = 0


    def GetFrame(self):
        start_time = time.time()
        self.MakeFrameEffect()
        tot_time = time.time() - start_time
        if (tot_time < self.speed):
            time.sleep(self.speed - tot_time)
        return self.frame


    def MakeFrameEffect(self):
        M = np.float32([
            [1, 0, 1],
            [0, 1, 0]
        ])
        self.frame = cv2.warpAffine(self.frame, M, (self.frame.shape[1], self.frame.shape[0]))
        cv2.line(self.frame, (0, 0), (0, self.h), self.current_color, 1)
        self.xpos += 1
        if (self.xpos == self.linethick):
            self.xpos = 0
            if (self.current_color == self.RED):
                self.current_color = self.WHITE
            else:
                self.current_color = self.RED