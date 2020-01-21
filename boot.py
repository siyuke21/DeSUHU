"""
This file is executed on every boot
(including wake-boot from deepsleep)

So, do setup configuration for Board
at this file.
"""
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()