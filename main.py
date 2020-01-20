import os
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
    |- main.py
    |- ....
"""
disk = SDCard(SPI(1), Pin(15))
os.mount(disk, '/disk')

"""
"""
dht = DHT11(Pin(2))

file_name = None
file = None

while True:
    """ Run Main Program """
    hour = datetime.get(datetime.HOUR)

    if hour == 0 or file_name is None:
        date = "{}-{}-{}".format(
            datetime.get(datetime.YEAR),
            datetime.get(datetime.MONTH),
            datetime.get(datetime.DAY))
        file_name = "/disk/data-{}-{}".format(date, str(hour))
        file = open(file_name, 'w')

    else:
        file = open(file_name, 'a')

    dht.measure()
    humidity = dht.humidity()
    temperature = dht.temperature()
    date_time = datetime.get_datetime()

    file.write("{};\thumidity:{};\ttemperature:{};".format(
        str(date_time), str(humidity), str(temperature)))
    file.close()

    # Delay for 5 Minute
    sleep(300)