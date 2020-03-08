import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN)

prev_input = 0

while True:
    input = GPIO.input(21)

    if ((not prev_input) and input):
        print("Wollah pressure G!")

    prev_input = input

    time.sleep(0.10)

