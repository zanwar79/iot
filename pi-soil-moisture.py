import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
MSENSOR=8
LEDDRY=10
LEDMOIST=12
GPIO.setup(MSENSOR, GPIO.IN)
GPIO.setup(LEDDRY, GPIO.OUT)
GPIO.setup(LEDMOIST, GPIO.OUT)

try:
    while True:
        time.sleep(0.1)
        #if moisture detected output is low
        if GPIO.input(MSENSOR) == False:
            GPIO.output(LEDMOIST, 1)
            GPIO.output(LEDDRY,0)
        elif GPIO.input(MSENSOR) == True:
            GPIO.output(LEDMOIST, 0)
            GPIO.output(LEDDRY,1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting")
    exit
