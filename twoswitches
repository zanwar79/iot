# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.IN)

# while loop to constantly check pins
while True:
    if (GPIO.input(3) and GPIO.input(7) ) == GPIO.HIGH:
    # flash output pin 5
        GPIO.output(5, GPIO.HIGH)

    else:
        GPIO.output(5, GPIO.LOW)
