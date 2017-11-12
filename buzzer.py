import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
button1=12      # Give intuitive names to our pins
GPIO.setup(3,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(button1,GPIO.IN,pull_up_down=GPIO.PUD_UP)  
try:
    while True:
        if GPIO.input(button1) == GPIO.LOW:
            print("button 1 was pressed")
            GPIO.output(3,GPIO.HIGH)
        else:
            GPIO.output(3,GPIO.LOW)

        GPIO.output(7,GPIO.LOW)
        time.sleep(.3)
        GPIO.output(7,GPIO.HIGH)
        time.sleep(.3)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit
