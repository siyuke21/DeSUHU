"""
This file is executed on every boot
(including wake-boot from deepsleep)

So, do setup configuration for Board
at this file.
"""

import gc
import esp
import network

from machine import Pin
from time import sleep

esp.osdebug(None)
gc.collect()