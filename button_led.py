import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
led_pin = 18
button_pin = 23  # Use the pin number you've connected the button to

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Set pull-down resistor

try:
    while True:
        if GPIO.input(button_pin):  # Button is pressed if True
            GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on
        else:
            GPIO.output(led_pin, GPIO.LOW)  # Turn LED off
except KeyboardInterrupt:
    # Clean up the GPIO on Ctrl+C exit
    GPIO.cleanup()
