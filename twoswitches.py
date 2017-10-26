# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# while loop to constantly check pins
while True:
    if (GPIO.input(8) and GPIO.input(10) ) == GPIO.HIGH:
    # flash output pin 5
        GPIO.output(5, GPIO.HIGH)

    else:
        GPIO.output(5, GPIO.LOW)
