from time import sleep  # Library will let us put in delays
import RPi.GPIO as GPIO # Import the RPi Library for GPIO pin control
GPIO.setmode(GPIO.BOARD)# We want to use the physical pin number scheme
LED1=22
GPIO.setup(LED1,GPIO.OUT) # LED1 will be an output pin
pwm1=GPIO.PWM(LED1,1000)  # We need to activate PWM on LED1 so we can dim, use 1000 Hz 
pwm1.start(0)              # Start PWM at 0% duty cycle (off)             
bright=1.0                   # Set initial brightness to 1%

def timer (pin): # Create a new function
    reading = 0.0    # Create our counter and set it to zero
    GPIO.setup(pin, GPIO.OUT) # Set the pin to output
    GPIO.output(pin, GPIO.LOW) # Set the pin to low to discharge the capacitor
    sleep(0.1) # wait for 100ms whilst the capacitor discharges
    GPIO.setup(pin, GPIO.IN) # Set the pin to input
    while (GPIO.input(pin) == GPIO.LOW): # keep looping until the capacitor is charged and the input hits high
        reading += 1.0 # add one to our counter each loop
    return reading # when the loop finishes, return the reading

while True:
	capacitance = input("Select which size capacitor you are using\n1. Large Black (100uF)\n2. Small Black (33uF)\n3. Brown Ceramic (1uF)\n")
	if capacitance == 1:
		capacitance = 1000000
		break;
	elif capacitance == 2:
		capacitance = 500000
		break;
	elif capacitance == 3:
		capacitance = 200
		break;
	else:
		print("\nSorry your input is not valid")

while(1):                  # Loop Forever
	result = timer(10)
	bright = result/capacitance * 100   #large black capacitor
	print("Current level of darkness out of 100", bright)
	if bright>100:                 # Keep Brightness at or below 100%
		bright=100
	pwm1.ChangeDutyCycle(bright)  # Apply new brightness
