import cv2
import numpy as np
import neopixel_serial
import time
import json
import os
import sys
sys.path.append("effects/")
from rainbow import Rainbow
from red_white_bars import RedWhiteBars
from color_top_down import ColorTopDown
from random_color_jump import RandomColorJump


#   SETTINGS START
LED_NUMBER = 56
LED_PORT = "COM3"
LED_SPEED = "250000"
LED_BRIGHTNESS = 6
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
SHOW_VIDEO = True
#   SETTINGS END


#   Initialize NeoPixel
strip = neopixel_serial.NeoSerial(LED_NUMBER, LED_PORT, LED_SPEED)
strip.SetBrightness(LED_BRIGHTNESS)

time.sleep(1)

leds = []

#   Read all JSON file we find in current folder: put all LEDs into leds list with OffsetX and OffsetY
json_files = [pos_json for pos_json in os.listdir(".") if pos_json.endswith('.json')]
for json_file in json_files:
    with open(json_file) as leds_file:
        print("Read file: " + json_file)
        LEDGroup = json.load(leds_file)
        for led in LEDGroup["LEDS"]:
            leds.append((led[0] + LEDGroup["OffsetX"], led[1] + LEDGroup["OffsetY"]))

#   Check if LED number is correct
if (LED_NUMBER != len(leds)):
    print("ERROR: wrong LED_NUMBER")
    exit(0)

#   Initialize the light effect
effect = Rainbow(w = FRAME_WIDTH, h = FRAME_HEIGHT, speed = 0.01)
#effect = RedWhiteBars(w = FRAME_WIDTH, h = FRAME_HEIGHT, speed = 0.01, thickness = 100)
#effect = ColorTopDown(w = FRAME_WIDTH, h = FRAME_HEIGHT, speed = 0.002, color = (200, 200, 200))
#effect = RandomColorJump(w = FRAME_WIDTH, h = FRAME_HEIGHT, speed = 0.002)

#   Start the show
TmrUpdateLEDs = time.time()
while (True):

    #   Get frame effect
    frame = effect.GetFrame()
    if SHOW_VIDEO:
        f = frame.copy()
        mask = np.zeros(f.shape[:2], dtype="uint8")

    #   For each LED...
    c = 0
    for led in leds:
        #   Get ROI frame color and send to neopixel
        roi = frame[led[1]-2:led[1]+2, led[0]-2:led[0]+2]
        color = cv2.mean(roi)
        strip.Set(c, (int(color[2]), int(color[1]), int(color[0])))
        c += 1
        #   Print circles on mask
        if SHOW_VIDEO:
            #cv2.circle(mask, (led[0], led[1]), 4, (255,255,255), -1)
            cv2.circle(f, (led[0], led[1]), 4, (255,255,255), -1)

    #   Update NeoPixels (low frequency)
    if (time.time() >= TmrUpdateLEDs):
        TmrUpdateLEDs = time.time() + 0.1
        strip.Show()
        
    #   Show debug frame on video
    if SHOW_VIDEO:
        masked = cv2.bitwise_and(f, f, mask=mask)
        cv2.imshow("Frame (Press q for quit)", f)

    #   If press q: exit the cycle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


strip.SetAll((0, 0, 0))
strip.Show()
cv2.destroyAllWindows()




