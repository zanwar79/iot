# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.OUT)

# while loop to constantly check pins
while True:
    if GPIO.input(8) == GPIO.HIGH:
    # flash output pin 10
        GPIO.output(10, GPIO.HIGH)
    else:
        GPIO.output(10, GPIO.LOW)
