#! /usr/bin/python3

from oocsi import OOCSI
from OOCSIListener import Listener

# Definition of the event handlers

def onCuttingVolume(sender, event):
    print('Cutting volume event!')

def onSoundSpectrum(sender, event):
    print('Sound Spectrum event!')

def onBoardWeight(sender, event):
    print('Board Weight event!')

def onCuttingSpeed(sender, event):
    print('Cutting Speed event!')


receiver_channels = {'cuttingVolumeChannel': onCuttingVolume,
        'soundSpectrumChannel' : onSoundSpectrum, 
        'boardWeightChannel' : onBoardWeight, 
        'cuttingSpeedChannel' : onCuttingSpeed}

listener = Listener(receiver_channels)

