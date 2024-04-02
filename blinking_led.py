import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led_pin = 18

GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second

        # Turn the LED off
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second
except KeyboardInterrupt:
    # Clean up the GPIO on Ctrl+C exit
    GPIO.cleanup()
