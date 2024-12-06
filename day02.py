from machine import Pin

# Setup of output pin; pin 14 controls block LED
blockLED = Pin(14, Pin.OUT)
blockLED.value(0)
print("Block LED on!")