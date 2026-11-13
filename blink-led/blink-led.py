from machine import Pin
import time

# Create a Pin object for the onboard LED
# "LED" is a special name in MicroPython for Pico/Pico W's onboard LED
led = Pin("LED", Pin.OUT)

try:
    while True:
        led.on()          # Turn LED on
        time.sleep(0.5)   # Wait 0.5 seconds
        led.off()         # Turn LED off
        time.sleep(0.5)   # Wait 0.5 seconds
except KeyboardInterrupt:
    # Gracefully handle Ctrl+C in REPL
    led.off()
    print("Blink stopped.")
