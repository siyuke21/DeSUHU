import os
import run
import datetime

from sdcard import SDCard
from machine import Pin, SPI
from dht import DHT11
from time import sleep


"""
Initialize SD Card Module at SPI 1 and Pin 15.
And then Mounting SD Card to directory disk.
Now list directory at root :
- /
    |- disk/
    |- boot.py
    |- run.py
    |- ....
"""
MOUNT_DIR = '/disk'
disk = SDCard(SPI(1), Pin(15))
os.mount(disk, MOUNT_DIR)

"""
Initialize DHT11 Module 
to Read Humidity and Temperature.
Where, there are 3 useful function such as :
- measure(): To Read and Calculate humidity and temperature
- humidity(): Getting the result of calculating humidity
- temperature(): Getting the result of calculating temperature
"""
dht = DHT11(Pin(2))

file_name = None
mode = None

while True:
    """
    This looping run the board 
    to get and save data humidity and temperature
    after setup configuration success at file boot.py 
    """
    hour = datetime.get(datetime.HOUR)

    if hour is 0 or file_name is None:
        date = datetime.get_date()
        listdir = os.listdir(MOUNT_DIR)
        file_name = "{}/data-{}".format(MOUNT_DIR, date)
        listdir = list(filter(lambda name: "data-".format(date) in name, listdir))

        if len(listdir) is 0:
            mode = 'w'
        else:
            mode = 'a'

    else:
        mode = 'a'

    run.get_data(dht, file_name, mode)

    # Delay for 5 Minute
    sleep(5)