from lib import MOUNT_DIR
from time import sleep
from utils import IO
from utils import Sensor

from boot import ds
from boot import dht

sensor = Sensor()

def loop():
    file_name = "{}/data-{}.txt".format(MOUNT_DIR, ds.DateTime())
    io = IO(path=file_name)

    if ds.Hour() == 0:
        io.set_mode('w')

    # read data from sensor dht 
    # and save to variable data.
    data = sensor.read_dht()

    # Write data to file
    io.save(data)

    # Delay for 5 Second
    sleep(5)


""" Run Device """
while True:
    loop()