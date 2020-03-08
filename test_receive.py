#! /usr/bin/python3

from oocsi import OOCSI
import sys

if len(sys.argv) < 2:
    print('usage:', sys.argv[0], '<channel>')
    exit()

oocsi = OOCSI('Testerinator', 'oocsi.id.tue.nl')

def printMessage(sender, recipient, event):
    print('from', sender, '->', event)
    
oocsi.subscribe(sys.argv[1], printMessage)
