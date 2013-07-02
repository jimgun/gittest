#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep

def ledInit():
    
    GPIO.setmode(GPIO.BCM)
    #IO24 -> red
    GPIO.setup(24, GPIO.OUT)
    #IO23 -> green
    GPIO.setup(25, GPIO.OUT)
    #IO18 -> yellow
    GPIO.setup(18, GPIO.OUT)
    
def setRedLed( state ):
    GPIO.output( 24, state )
    
def setGreenLed( state ):
    GPIO.output( 25, state )

def setYellowLed( state ):  
	GPIO.output( 18, state )

if __name__ == "__main__":
    ledInit()
    
    for i in range(1,20):
        setRedLed(i%2)
        setGreenLed(i%2)
        setYellowLed(i%2)
        sleep(.1)
        
        setRedLed(1+i%2)
        setGreenLed(1+i%2)
        setYellowLed(1+i%2)
        sleep(.1)
    
    setRedLed(0)
    setGreenLed(0)
    setYellowLed(0)
    
    GPIO.cleanup()

