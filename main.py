#! /usr/bin/python3

from oocsi import OOCSI
from OOCSIListener import Listener
from EventHandlers import *
from PressureSensor.pressure_sensor import PressureSensorThread 
from state import StorageUnitState
import time

# Obtain oocsi instance and connect to remote server
oocsi = OOCSI('SmartStorageUnit', 'oocsi.id.tue.nl')

# Initialize the global state 
global_state = StorageUnitState(oocsi)

evt = EventHandler(global_state)

# Dictionary of which channels to receive on and their event handlers
receiver_channels = {
        'cuttingVolumeChannel': evt.onCuttingVolume,
        'soundSpectrumChannel' : evt.onSoundSpectrum, 
        'boardWeightChannel' : evt.onBoardWeight, 
        'cuttingSpeedChannel' : evt.onCuttingSpeed
        }

# Start the OOCSI listener
listener = Listener(oocsi, receiver_channels)

# Start the pressure sensor thread with sensor on GPIO 21
psensor = PressureSensorThread(21)
# psensor = 0 # use for testing without RPi

# Sensor loop
while True:
    if (psensor):
        if (psensor.new and (psensor.state > 0)):
            global_state.items = state
            print('item added!', global_state.items)
        elif (psensor.new and (psensor.state <= 0)):
            global_state.items = state
            print('item removed!', global_state.items)




