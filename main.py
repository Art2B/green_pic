import time
from gpiozero import Button
from signal import pause
import os

photoDirPath = "./results/"
button = Button(2)

def take_picture():
    filename = str(int(time.time() * 1000))
    os.system("fswebcam -r 1920x1080 --no-banner " + photoDirPath + filename + ".jpg")
    print("Saved picture " + filename)

print("Script is up.")

button.when_pressed = take_picture
pause()
