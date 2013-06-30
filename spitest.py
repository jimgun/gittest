#!/usr/bin/python

import spidev

spi = spidev.SpiDev()
spi.open(0,0)
print spi.xfer2([0,1,2,3,4])

