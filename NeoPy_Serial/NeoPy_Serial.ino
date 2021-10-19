#include <Adafruit_NeoPixel.h>

//      BEGIN SETUP
#define LEDS 56
#define PIN 2
//      END SETUP


Adafruit_NeoPixel strip = Adafruit_NeoPixel(LEDS, PIN, NEO_GRB + NEO_KHZ800);

long unsigned int packetSize;
int r, g, b;
char packetBuffer[LEDS*3];

void setup() {

  Serial.begin(250000);

  strip.begin();
  strip.setBrightness(255);
  strip.show();
 
}



void loop() {

  while(Serial.available()) {

    packetBuffer[packetSize] = Serial.read(); 
    packetSize++;
    
    if (packetSize == LEDS * 3) {
      packetSize = 0;
      for (int i=0; i<LEDS * 3; i+=3) {
          r = (int)(byte*)(packetBuffer)[i];
          g = (int)(byte*)(packetBuffer)[i+1];
          b = (int)(byte*)(packetBuffer)[i+2];
          strip.setPixelColor(i/3, strip.Color(r, g, b));
      }
      strip.show();
    }
    
  }

}
