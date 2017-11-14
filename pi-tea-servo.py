import RPi.GPIO as GPIO
import time

servo  =  7
led    = 10
button = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo, GPIO.OUT)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)

p = GPIO.PWM(7, 50)
p.start(7.5)

try:
	while True:
		if GPIO.input(button) == 0:    #if button pressed
			GPIO.output(led,1)     #light the led
			p.ChangeDutyCycle(7.5) #Neutral Position
			time.sleep(1)
			p.ChangeDutyCycle(12.5) #180
			time.sleep(1)
			p.ChangeDutyCycle(2.5)  #0
			time.sleep(1)
		else:			       #if button not pressed
			GPIO.output(led,0)     #turn led off

except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
