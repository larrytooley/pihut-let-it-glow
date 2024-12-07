# Imports
from machine import Pin
import time

greenbutton = Pin(3, Pin.IN, Pin.PULL_DOWN)

while True:
    
    time.sleep(0.2) # Short Delay
        
    if greenbutton.value() == 1:
        
        print("Green button pressed")
        
    else: # If no buttons are being pressed
        
        print("No button press")