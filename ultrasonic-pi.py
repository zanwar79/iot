import RPi.GPIO as GPIO
import time
import datetime

#Setup the GPIO to use the board numbering
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#Create Variables
global distance
 
LED1 = 22
GPIO_TRIGGER = 16
GPIO_ECHO = 18

#Setup GPIO pins 
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

#Ultrasonic Sensor
def ultra(sensor):
    global distance
    if sensor == 0:

	time.sleep(0.3)
	stop = 0
	start = 0

	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = time.time()
	while GPIO.input(GPIO_ECHO)==0:
            start = time.time()

	while GPIO.input(GPIO_ECHO)==1:
            stop = time.time()

	# Calculate pulse length
	elapsed = stop-start

	# Distance pulse travelled in that time is time
	# multiplied by the speed of sound (cm/s)
	distance = elapsed * 34000

	# That was the distance there and back so halve the value
	distance = distance / 2

	return distance

    else:
        print "Error!!!!!!"

#LED Blink
def blink(pin,duration):  
    for i in range(0,3):
        GPIO.output(pin,GPIO.HIGH)  
        time.sleep(duration)  
        GPIO.output(pin,GPIO.LOW)  
        time.sleep(duration)  
        return  


def reset(pin):
	GPIO.output(pin, GPIO.LOW)

#Cue to tell me that the system is ready
reset(LED1)

try:
    while True:
	ultra(0)
        print(distance)
	if distance <= 4:
            blink(LED1, 0.1)
        elif 4 < distance <= 7: 
            blink(LED1, 0.2)
        elif 7 < distance <= 10: 
            blink(LED1, 0.3)
        elif 10 < distance < 15: 
            blink(LED1, 0.4)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting")
    exit
