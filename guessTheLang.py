from time import sleep
import os
import random
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
# GPIO2 for Indicator LED
GPIO.setup(2, GPIO.OUT)

# GPIO3 for 'New Track' button
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(2, GPIO.LOW)

trackNum = 0

#tracks = [ 'arabic.mp3', 'english.mp3', 'french.mp3', 'german.mp3', 'hindi.mp3', 'italian.mp3',
# 'japanese.mp3', 'mandarin.mp3', 'portuguese.mp3', 'russian.mp3', 'spanish.mp3']

tracks = [ 'arabic.mp3', 'english.mp3', 'french.mp3', 'german.mp3', 'hindi.mp3', 'japanese.mp3', 'mandarin.mp3', 'russian.mp3', 'spanish.mp3']

#langToPin = [14, 15, 18, 23, 24, 25, 8, 7, 11, 9, 10]

langToPin = [14, 15, 18, 23, 24, 25, 8, 7, 11]

print ("Starting up with Tracks: ")
print (tracks)
    

while True:
#    input_value = GPIO.input(18)
#    print(GPIO.input(18))
    #sleep(0.1)
    if GPIO.input(3) == GPIO.LOW:
        print("'New Track' button press detected")
        while GPIO.input(3) == GPIO.LOW:
            print("Waiting for the 'New Track' button to be released")
            # Wait for key release
            sleep(0.1)
        trackNum = random.randint(0,len(tracks) - 1)
	print("TrackNum = ")
	print(trackNum)
	print("Tracks[trackNum] = ")
	print(tracks[trackNum])
        print("Stopping previous instance of mpg321 (if any)")
        os.system('sudo pkill -SIGHUP mpg321 #stop')
        print("Previous instance of mpg321 (if any) stopped")
        
        os.system('mpg321 /home/pi/GuessTheLang/' + tracks[trackNum] + ' &')
        print("Playing MP3")

    if GPIO.input( langToPin[trackNum] ) == GPIO.LOW:
        print("Correct 'Language' button press detected")
        print("langToPin[trackNum] =")
        print(langToPin[trackNum])
        GPIO.output(2, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        sleep(0.2)
        GPIO.output(2, GPIO.HIGH)
        sleep(0.2)
        GPIO.output(2, GPIO.LOW)
        sleep(0.2)
