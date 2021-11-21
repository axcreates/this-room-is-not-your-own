from picamera import PiCamera
from gpiozero import Button
import RPi.GPIO as GPIO
from time import sleep
import datetime
import os

camera = PiCamera()
camera.rotation = 180

button = Button(21)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN)
GPIO.setup(12, GPIO.IN)
drawerInLast = GPIO.input(16)
chairInLast = GPIO.input(4)
bookInLast = GPIO.input(12)

camera.start_preview(alpha=100)
date = datetime.datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
sleep(3)

while True:
    def buttonpress():
        camera.capture('/home/pi/Desktop/Images/lamp' +date+ '.jpg')
    button.when_pressed = buttonpress
    #os.system("rclone copy /home/pi/Desktop/Images/ drive:room")

    drawerIn = GPIO.input(16)
    if (drawerIn == 1) and (drawerInLast == 0):
        camera.capture('/home/pi/Desktop/Images/drawer' +date+ '.jpg')
     #   os.system("rclone copy /home/pi/Desktop/Images/ drive:room")
    drawerInLast = drawerIn
    
    chairIn = GPIO.input(4)
    if (chairIn == 1) and (chairInLast ==0):
        camera.capture('/home/pi/Desktop/Images/chair' +date+ '.jpg')
     #   os.system("rclone copy /home/pi/Desktop/Images/ drive:room")
    chairInLast = chairIn
        
    bookIn = GPIO.input(12)
    if (bookIn == 0) and (bookInLast == 1):
        camera.capture('/home/pi/Desktop/Images/book' +date+ '.jpg')
      #  os.system("rclone copy /home/pi/Desktop/Images/ drive:room")
    bookInLast = bookIn
    
#    os.system("rclone copy /home/pi/Desktop/Images/ drive:room")

camera.stop_preview()
    