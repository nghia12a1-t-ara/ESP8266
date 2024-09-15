# import Libraries
from machine import Pin
import time
from time import sleep

# Setup LED is OUTPUT, default = LOW
led = Pin(2, Pin.OUT)

# Super Loop - Blink LED
while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)