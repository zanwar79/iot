import os, time, threading, random
from PIL import Image, ImageFont, ImageDraw
from random import shuffle

items=[]
displayItems=[]

def colorRed():
    return (255, 0, 0)

def colorGreen():
    return (0, 255, 0)

def colorBlue():
    return (0, 0, 255)

def colorRandom():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def writeImage(url, count):
    global displayItems
    bitIndex=0
    #link, headLine="", url[:]
    link, _, headLine = url.partition(" ")
	#link = some_string.partition(' ')[0].
    print("link",link)
    print("headline",headLine)
    def randCol(index = -1):
        if index % 3 == 0:
            return colorRed()
        elif index % 3 == 1:
            return colorGreen()
        elif index % 3 == 2:
            return colorBlue()
        else:
            return colorRandom()
    text = ((headLine, randCol(count)), (link, colorRandom()))
    text = ((headLine, randCol(count)), (link, colorRandom()))
    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
    all_text = ""
    for text_color_pair in text:
        t = text_color_pair[0]
        all_text = all_text + t
    width, ignore = font.getsize(all_text)
    im = Image.new("RGB", (width + 30, 16), "black")
    draw = ImageDraw.Draw(im)
    x = 0;
    for text_color_pair in text:
        t = text_color_pair[0]
        c = text_color_pair[1]
        draw.text((x, 0), t, c, font=font)
        x = x + font.getsize(t)[0]
    filename=str(count)+".ppm"
    displayItems.append(filename)
    im.save(filename)

def ticker():
	global displayItems
	print("Inside Ticker")
	while(True):
		print("Going to delete files")
		#delete all the image files
		os.system("find . -name \[0-9]*.ppm -delete")
		displayItems = []
		displayItems.append('griffin4.ppm')
		fo = open("today","r")
		events = [x.strip() for x in fo.readlines()]
		fo.close()
		counter =1 
		for event in events:
			writeImage(event,counter)
			print("Event and counter is ", event, counter)
			counter = counter +1
		showSquare()
		showOnLEDDisplay()
		time.sleep(30)

def showSquare():
	os.system("sudo ./led-matrix -t 10 -D 0")
		
def showOnLEDDisplay():
    for disp in displayItems:
        print("Going to display:",disp)
        os.system("sudo ./led-matrix -c 2 -t 10 -m 25 -D 1 "+disp)

if __name__ == '__main__':
	ticker()
#	print("Creating ticker thread")
#	t = threading.Timer(5.0, ticker)
#	t.daemon = True
#	t.start()
#	while True:
#		time.sleep(1)
