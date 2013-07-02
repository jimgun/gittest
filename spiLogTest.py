#!/usr/bin/python

import spidev
import datetime
import time
import random
import struct


def speedTest( txDataSize, numberOfTransmits, busSpeed, spidev):

    spi.max_speed_hz = busSpeed
    print "Sending %s bytes of data %s times with a bus speed of %s" % (txDataSize, numberOfTransmits, spi.max_speed_hz)
    txData = range(1,txDataSize)
    startTime = datetime.datetime.now()
    for i in range(0, numberOfTransmits):
        rxData = spi.xfer2(txData)
    endTime = datetime.datetime.now()
    print "execution time: %s" % (endTime-startTime)
    print "bytes sent: %s" % (txDataSize*numberOfTransmits)
    #print "transfer speed: %.2fkb/s" % int(int(txDataSize)*int(numberOfTransmits)/1024)/ int((endTime-startTime).microseconds/1000) 


def logSpiData( filename, level, numberOfTransmits, busSpeed, spidev):
    spi.max_speed_hz = busSpeed
    print "Sending %s bytes of data %s times with a bus speed of %s" % (4, numberOfTransmits, spi.max_speed_hz)
    levelString = "level = %s;\n" % level
    dataString = "data = ["
    random.seed()
    for i in range(0, numberOfTransmits):
        #txValue = random.randint(0,255)
        txValue = random.gauss(50,10)
        #print txValue
        txData = list(struct.unpack("4B", struct.pack("I", txValue)))
        xferTimeStamp = time.time() * 1000 # *1000 for javascript format...
        rxData = spi.xfer2(txData)
        #print rxData
        #print tuple(rxData)
        #print struct.pack("4b",*rxData)
        rxValue = struct.unpack("I", struct.pack("4B",*rxData))[0];
        #print "%s %s" % (xferTimeStamp, rxValue)
        dataString = "%s[%d,%d]," % (dataString, xferTimeStamp, rxValue)
    dataString = "%s[,]];\n" % dataString
    #print dataString
    
    f = open(filename, "w")
    f.write(dataString)
    f.write(levelString)
    f.close()

	

if __name__ == "__main__":
    spi=spidev.SpiDev()
    spi.open(0,0)

    logSpiData("/var/www/data.js", 55, 2000, 5000000, spidev)
    


