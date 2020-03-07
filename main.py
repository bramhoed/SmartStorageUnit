#! /usr/bin/python3

from oocsi import OOCSI
from OOCSIListener import Listener
from  EventHandlers import *
from recipe import Recipe

# Dictionary of which channels to receive on and their event handlers
receiver_channels = {
        'cuttingVolumeChannel': onCuttingVolume,
        'soundSpectrumChannel' : onSoundSpectrum, 
        'boardWeightChannel' : onBoardWeight, 
        'cuttingSpeedChannel' : onCuttingSpeed
        }

# Start the event listener
listener = Listener(receiver_channels)

# Are we cooking something?
current_recipe = Recipe('example_recipe.json')
print(current_recipe.recipe_text)




