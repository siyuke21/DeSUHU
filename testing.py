import os
import run
import network

from sdcard import SDCard
from machine import Pin, SPI
from dht import DHT11
from time import sleep
from datetime import DateTime

"""
Just to Testing via `repl`
"""

def should_work():
    MOUNT_DIR = '/disk'
    disk = SDCard(SPI(1), Pin(15))
    os.mount(disk, MOUNT_DIR)


    led = Pin(2, Pin.OUT)
    SSID = "12345678"
    PASSWORD = "matematika"

    net = network.WLAN(network.STA_IF)
    net.active(True)
    sleep(5)
    print("Network Is Active = {}".format(net.active()))

    if net.active():
        net.connect(SSID, PASSWORD)
        sleep(10)

        if net.isconnected():
            """
            In this case i will turn off the led lamp
            but I dont understand why micropython 
            use method on() to turn off the led lamp.
            """
            led.value(1)



    dht = DHT11(Pin(2))

    print("Network Is Connected = {}".format(net.isconnected()))
    datetime = DateTime(net.isconnected())
    file_name = None

    print("Setup Completed")

    while True:
        """
        This looping run the board 
        to get and save data humidity and temperature
        after setup configuration success at file boot.py 
        """
        hour = datetime.get(datetime.HOUR)

        if hour == 0 or file_name is None:
            date = datetime.get_date()
            listdir = os.listdir(MOUNT_DIR)
            listdir = list(filter(lambda name: "data-{}".format(date) in name, listdir))

            # Create File Name
            file_name = "{}/data-{}.txt".format(MOUNT_DIR, datetime.get_date())
            count = len(listdir)

            if count > 0:
                checking = "2000" in file_name or not net.isconnected()

                if checking and hour == 0:
                    file_name = "{}/data-{}_{}.txt".format(MOUNT_DIR, date, count)
                    mode = 'w'

                else:
                    mode = 'a'

            else:
                mode = 'w'

        else:
            mode = 'a'

        run.get_data(datetime.get_datetime(), dht, file_name, mode)

        # Delay for 5 Second
        sleep(5)