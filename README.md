# OpenCV NeoPixel Mapping

## Hardware (www.futurashop.it)
- USB webcam
- [Miniduino](https://www.futurashop.it/Atmega32u4-Miniduino-scheda-Arduino-Dongle-USB-7305-MINIDUINO)
- NeoPixels:   Chain,   [Star](https://www.futurashop.it/stella-natale-LED-neopixel-ft1300m),   [Strip](https://www.futurashop.it/NEOPIXEL_STRIP_RGB_STRIP150LED)
- Power supply @ 5 Volt:   [50 W](https://www.futurashop.it/alimentatore-switching-50w-5v-4125-mw05005),   [100 W](https://www.futurashop.it/alimentatore-switching-100w-5v-4125-mw10005-1)

## Setup
1) Connect power supply to NeoPixels (VCC and GND)
2) Connect NeoPixels signal to D2 on Miniduino and also NeoPixels GND to GND on Miniduino
3) Connect Miniduino to PC, select "Arduino Leonardo" board
4) Open NeoPy_Serial.ino sketch, configure LEDs number and upload the sketch
5) Connect webcam to PC and place it aligned in front of the NeoPixels both horizontally and vertically
6) Install [Python 3.x](https://www.python.org/downloads/) and required libraries ( `pip install pyserial` and `pip install opencv-python` )
7) Open terminal and go to the project folder
8) Start mapping the LEDs with command: `python map.py`
9) At the end a leds.json file will be saved
10) Start lights effect with the command: `python show.py`

## Tips
- You can use the view.py script to help you align the webcam in front of the NeoPixel object
- When you are mapping the brightness of the environment it's important! Make sure it's quite dark and that the brightness remains constant
- When you are mapping the LED brightness should not be very high, you can configure it in the initial parameters of the map.py script
- Once the mapping is complete, you will no longer need the webcam
- You can select the colored effects and the brightness of the LEDs by editing the show.py script
- You can map different NeoPixel objects at different times, remember to rename the leds.json file at the end of each mapping: the show.py script will load all the JSON files in its own folder
- If you have mapped several objects, so you have several JSON files, you can open them and edit their OffsetX and OffsetY parameters to translate them when you run show.py
