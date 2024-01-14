#Python3 GPIO state detection
#Simple Python Script to detect GPIO pin state change

import RPi.GPIO as GPIO
import time

# Use the Broadcom SOC channel
GPIO.setmode(GPIO.BCM)

# Set up the GPIO channel
GPIO.setup(27, GPIO.IN)

# Function to print when GPIO pin goes high or low
def print_status(channel):
    if GPIO.input(27):
        print("GPIO 27 went HIGH")
    else:
        print("GPIO 27 went LOW")

# Detect both rising and falling edge
GPIO.add_event_detect(27, GPIO.BOTH, callback=print_status)

try:
    while True:
        # Do nothing and let the callback handle GPIO changes
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
