#Import frameworks
from random import randint
import RPi.GPIO as GPIO
import time
 
#GPIO Setup
red_led = 3
green_led = 5
top_button = 8
bottom_button = 10
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(top_button, GPIO.IN,pull_up_down=GPIO.PUD_UP) #Top Button
GPIO.setup(bottom_button, GPIO.IN,pull_up_down=GPIO.PUD_UP) #Bottom Button
GPIO.setup(red_led, GPIO.OUT) #Red
GPIO.setup(green_led, GPIO.OUT) #Green
 
 
def game():
    #Random Number
    x = randint(0,9)
    #print(x)
    #Determine if number is even or odd
    y = x%2
 
    #Story
    print "You are casually walking down the street one day when out of nowhere you notice a ticking time bomb, ready to explode. You immediately remember your bomb squad days and rush into action. You have the bomb nearly defused, but you must now choose: red wire or green wire. You have 10 seconds."
    time.sleep(1)
    print "Choose wisely"
 
    #Button Controls
    while (GPIO.input(top_button) == True or GPIO.input(bottom_button) == True): #Listen for input from buttons
        topButtonState = GPIO.input(top_button)
        bottomButtonState = GPIO.input(bottom_button)
        if (topButtonState == False): #Top Button Pressed
            if (y == 0): #If the number was even and you pushed the top button, you lose
                print("You have failed. Countless people have died due to your incompetence and you have been reduced to nothing but a few subatomic particles that are barely visible to the human eye.")
                GPIO.output(red_led,GPIO.HIGH)
                time.sleep(.3)
            else: #If the number was odd and you pushed the bottom button, you win.
                print ("Well done! You have successfully defused the bomb and saved many lives. You are an international hero!")
                GPIO.output(green_led,GPIO.HIGH)
                time.sleep(.3)
        elif (bottomButtonState == False): #Button Button Pressed
            if (y == 1): #If the number was odd and you pushed the bottom button, you lose.
                print("You have failed. Countless people have died due to your incompetence and you have been reduced to nothing but a few subatomic particles that are barely visible to the human eye.")
                GPIO.output(red_led,GPIO.HIGH)
                time.sleep(.3)
            else: #If the number was even and you pushed the bottom button, you win.
                print ("Well done! You have successfully defused the bomb and saved many lives. You are an international hero!")
                GPIO.output(green_led,GPIO.HIGH)
                time.sleep(.3)
        time.sleep(.3) #Leave the light on for .3 second
        GPIO.output(green_led,GPIO.LOW) #Turn off Green
        GPIO.output(red_led,GPIO.LOW) #Turn off Red
 
    print "Exiting Game"
    return
game()
GPIO.cleanup()
