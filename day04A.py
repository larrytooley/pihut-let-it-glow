from machine import Pin
import time

# Set up the LED pins
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

# Create a list of our LEDs
segments = [seg1, seg2, seg3, seg4, seg5]

# For loop to turn each LED on one-by-one
for led in segments:
    
    led.value(1)
    time.sleep(.5)
    
# For loop to turn off all LEDs
    
for led in segments:
    
    led.value(0)
