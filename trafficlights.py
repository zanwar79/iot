# import modules
import RPi.GPIO as GPIO
import time

# setup pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

while True:
    for i in [3,5,7]:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(i, GPIO.LOW)


    for i in [7,5,3]:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(i, GPIO.LOW)
