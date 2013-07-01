#!/usr/bin/python

import spidev
import datetime


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



if __name__ == "__main__":
    spi=spidev.SpiDev()
    spi.open(0,0)

    print spi.max_speed_hz

    speedTest(256, 5, 50000, spidev)
    speedTest(256, 5, 100000, spidev)
    speedTest(256, 5, 500000, spidev)
    speedTest(256, 5, 5000000, spidev)
    speedTest(256, 5, 50000000, spidev)
    speedTest(256, 5, 500000000, spidev)

    speedTest(256, 100, 50000, spidev)
    speedTest(256, 100, 100000, spidev)
    speedTest(256, 100, 500000, spidev)
    speedTest(256, 100, 5000000, spidev)
    speedTest(256, 100, 50000000, spidev)
    speedTest(256, 100, 500000000, spidev)


