# Handling Bug Micropython when importing 'utils'
try:
    import utils

except:
    pass

from lib import MOUNT_DIR
from time import sleep
from utils.file import File
from utils.sensor import Sensor

from boot import ds
from boot import dht

sensor = Sensor(dht)

def loop():
    date = "{}-{}-{}".format(ds.Day(), ds.Month(), ds.Year())
    time = "{}-{}-{}".format(ds.Hour(), ds.Minute(), ds.Second())

    file_name = "{}/data-{}.txt".format(MOUNT_DIR, date)
    io = File(path=file_name)

    # read data from sensor dht 
    # and save to variable data.
    data = sensor.read_dht(time)

    # Write data to file
    io.save(data)

    # Delay for 5 Second
    sleep(5)


""" Run Device """
while True:
    loop()