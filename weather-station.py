import Adafruit_DHT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
DHTSENSOR=4  #(7 according to board)
# We need to supply 4 because the DHT library only supports BCM Numbering
LEDHOT=8
LEDCOLD=10
LEDHUMID=12
GPIO.setup(LEDHOT, GPIO.OUT)
GPIO.setup(LEDCOLD, GPIO.OUT)
GPIO.setup(LEDHUMID, GPIO.OUT)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, DHTSENSOR)
        print('Temp:' + str(temperature) + 'C' + ', Humidity:' + str(humidity))
        if temperature > 20:
            GPIO.output(LEDHOT, 1)
            GPIO.output(LEDCOLD,0)
        if temperature <=20:
            GPIO.output(LEDHOT, 0)
            GPIO.output(LEDCOLD,1)
        if humidity >50:
            GPIO.output(LEDHUMID,1)
        if humidity <=50:
            GPIO.output(LEDHUMID,0)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exiting")
    exit
