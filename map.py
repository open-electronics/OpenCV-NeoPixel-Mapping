import cv2
import numpy as np
import neopixel_serial
import time
import json


#   SETTINGS START
LED_NUMBER = 56
LED_PORT = "COM3"
LED_SPEED = "250000"
LED_BRIGHTNESS = 10
CAMERA_ID = 0
DELAY_LED = 0.1
DELAY_PROCESS = 0.2
THRESH_MARGIN = 0.6
SHOW_VIDEO = True
#   SETTINGS END




Save = {}
Save["OffsetX"] = 0
Save["OffsetY"] = 0

#   Initialize NeoPixel
strip = neopixel_serial.NeoSerial(LED_NUMBER, LED_PORT, LED_SPEED)
strip.SetBrightness(LED_BRIGHTNESS)

time.sleep(2)

#   Capture one frame with all LEDs switched off
cap = cv2.VideoCapture(CAMERA_ID, cv2.CAP_DSHOW)
ret, StartFrame = cap.read()
StartFrame = cv2.cvtColor(StartFrame, cv2.COLOR_BGR2GRAY)

StartCircleFrame = StartFrame.copy()

time.sleep(1)

TimerLED = time.time()
TimerProcess = time.time() 
LEDSet = False
MapStop = False
Counter = 0
leds = []

while (True):

    #   Get new frame
    ret, frame = cap.read()
    
    #   Check if it's time to switch on another LED
    if(time.time() - TimerLED >= DELAY_LED and not LEDSet and not MapStop):
        print("")
        print("Switch on LED " + str(Counter))
        #   Switch on LED
        strip.Set(Counter, (255, 255, 255))
        strip.Show()
        LEDSet = True
        TimerProcess = time.time() 


    #   Check if it's time to search and process for a LED
    if(time.time() - TimerProcess >= DELAY_PROCESS and LEDSet and not MapStop):
        print("Process LED " + str(Counter))
        #   Convert frame into grey
        grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #   Subtract current frame with the StartFrame
        grey_img = cv2.subtract(grey_img, StartFrame)
        
        #   Search for the brightest point in the frame and make a threshold
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(grey_img)
        thresh = maxVal * THRESH_MARGIN

        #   Put a threshold in the frame
        retval, threshold = cv2.threshold(grey_img, thresh, 255, cv2.THRESH_BINARY)
        threshold = cv2.GaussianBlur(threshold, (75,75), 15)

        #   Look for the center coordinates of the LED
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(threshold)
        leds.append(maxLoc)
        if SHOW_VIDEO:
            #cv2.imshow('LED threshold', threshold)
            pass

        #   Switch off the  LED
        strip.Set(Counter, (0, 0, 0))
        strip.Show()

        TimerLED = time.time()
        LEDSet = False

        Counter += 1
        if (Counter >= strip.NumPixels()):
            MapStop = True

    #   Update the screen drawing the LEDs we have found
    if SHOW_VIDEO:
        for led in leds:
            cv2.circle(StartCircleFrame, led, 5, (120,120,120), 2)
        cv2.imshow("Mapping... (Press q for quit)", StartCircleFrame)

    #   If press q or the mapping stops: exit the cycle
    if cv2.waitKey(1) & 0xFF == ord('q') or MapStop:
        break


#   Save frame dimensions and LEDs coordinates to JSON file
if (len(leds) == LED_NUMBER):
    Save["LEDS"] = [led for led in leds]
    with open("leds.json", "w") as outfile:
        json.dump(Save, outfile)
    print("Saved " + str(len(leds)) + " LEDs.")
else:
    print("ERROR: not enough LEDs mapped.")

#   Release the webcam
cap.release()
cv2.destroyAllWindows()
