from time import sleep  # Library will let us put in delays
from random import uniform
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme

LED=7
rightbutton=8
leftbutton=10
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(rightbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(leftbutton,GPIO.IN,pull_up_down=GPIO.PUD_UP)  

GPIO.output(LED, GPIO.HIGH)
sleep(uniform(5,15))
GPIO.output(LED, GPIO.LOW)

while(True):
    if (GPIO.input(leftbutton) == GPIO.LOW):
        print("Player left won the game")
        break

    if (GPIO.input(rightbutton) == GPIO.LOW):
        print("Player right won the game")
        break

GPIO.cleanup()
