#! /usr/bin/python3

from oocsi import OOCSI
from OOCSIListener import Listener
from  EventHandlers import *



receiver_channels = {'cuttingVolumeChannel': onCuttingVolume,
        'soundSpectrumChannel' : onSoundSpectrum, 
        'boardWeightChannel' : onBoardWeight, 
        'cuttingSpeedChannel' : onCuttingSpeed}

listener = Listener(receiver_channels)

