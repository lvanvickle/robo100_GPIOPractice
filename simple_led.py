import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
led_pin = 18  # Use the pin number you've connected the LED to

# Set up the LED pin as an output
GPIO.setup(led_pin, GPIO.OUT)

# Turn on the LED
GPIO.output(led_pin, GPIO.HIGH)

# Keep the LED on for 5 seconds
time.sleep(5)

# Clean up the GPIO to reset the pin
GPIO.cleanup()
