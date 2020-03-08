import RPi.GPIO as GPIO
import time
import threading


class PressureSensorThread:
    """
    Class that starts a thread to continully poll a pressure sensor

    Attributes:
    input_pin (int): Pin number of to which the pressure sensor is connected
    thread (Thread): Thread object for the polling thread

    state (int): Wheter or not sensor is under pressure

    """

    def __init__(self, pin):
        self.input_pin = pin

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN)
        
        self.thread = threading.Thread(target=self.pollSensor)
        self.thread.start()


    def pollSensor(self):

        prev_state = 0

        while True:
            state = GPIO.input(self.input_pin)

            if ((not prev_state) and state):
                print("Wollah pressure G!")
            elif ((not state) and prev_state):
                print("Wollah geen pressure G!")

            prev_state = state

            time.sleep(0.10)

