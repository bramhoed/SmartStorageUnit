#! /usr/bin/python3

from oocsi import OOCSI
from OOCSIListener import Listener
from  EventHandlers import *
from recipe import Recipe
from PressureSensor.pressure_sensor import PressureSensorThread 

# Dictionary of which channels to receive on and their event handlers
receiver_channels = {
        'cuttingVolumeChannel': onCuttingVolume,
        'soundSpectrumChannel' : onSoundSpectrum, 
        'boardWeightChannel' : onBoardWeight, 
        'cuttingSpeedChannel' : onCuttingSpeed
        }

# Start the event listener
listener = Listener(receiver_channels)

# Start the pressure sensor thread with sensor on GPIO 21
PressureSensorThread(21)

# Are we cooking something?
current_recipe = Recipe('example_recipe.json')




