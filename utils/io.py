import os

class IO :
    
    def __init__(self, path='/', mode='a'):
        self.path = path
        self.mode = mode

    def set_path(self, path):
        self.path = path

    def set_mode(self, mode):
        self.mode = mode

    def save(self, data):
        self.file = open(self.path, self.mode)

        try:
            self.file.write(data)
            print("No Error when writing data to disk")
        
        except:
            print("Error When Writing Data to disk")

        finally:
            file.close()