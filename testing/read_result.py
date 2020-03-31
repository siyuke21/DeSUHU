import os

from sdcard import SDCard
from machine import Pin, SPI

"""
class ini digunakan untuk melakukan checking result
via 'repl'
"""

class Reading:

    mount_dir = '/disk'

    def __int__(self):
        pass

    def get_file(self):
        os.mount(SDCard(SPI(1), Pin(15)), self.mount_dir)

        listdir = os.listdir(self.mount_dir)
        listdir = filter(lambda name: 'data-' in name, listdir)
        listdir = list(listdir)

        return listdir

    def execute(self):
        for file_name in self.get_file():
            print("{}/{}".format(self.mount_dir, file_name))

            try:
                file = open("{}/{}".format(self.mount_dir, file_name), 'r')
                content = file.read()
                print(content)

            except:
                print('Data Terlalu Panjang')

            finally:
                file.close()

    def delete(self):
        result = list(filter(lambda name: '2000' in name, self.get_file()))

        for filename in result:
            os.remove("{}/{}".format(self.mount_dir, filename))