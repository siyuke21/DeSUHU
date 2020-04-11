"""
This file is executed on every boot
(including wake-boot from deepsleep)

So, do setup configuration for Board
at this file.
"""

import gc
import os
import esp
import network

from lib import *
from machine import Pin
from machine import SPI

esp.osdebug(None)
gc.collect()

""" Mount SDCard to directory /disk """
_disk = SDCard(SPI(1), Pin(15))
os.mount(_disk, MOUNT_DIR)

_PIN_CLK = Pin(5)    # Pin CLK => D1
_PIN_DIO = Pin(4)    # Pin DIO => D2
_PIN_CS = Pin(0)     # Pin RST => D4 / D3

ds = DS1302(clk=_PIN_CLK, dio=_PIN_DIO, cs=_PIN_CS)
dht = DHT11(Pin(2))