"""
This file is executed on every boot
(including wake-boot from deepsleep)

So, do setup configuration for Board
at this file.
"""

import gc
import esp
import network

esp.osdebug(None)
gc.collect()

""" Mounting Storage Disk """
from lib import SDCard
from lib import MOUNT_DIR
from machine import Pin
from machine import SPI


disk = SDCard(SPI(1), Pin(15))
os.mount(disk, MOUNT_DIR)