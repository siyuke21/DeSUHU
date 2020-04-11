import os

class File:
    
    def __init__(self, path='/', mode='w'):
        self.path = path
        self.mode = mode

    def set_path(self, path):
        self.path = path

    def set_mode(self, mode):
        self.mode = mode

    def _is_exist(self):
        directory = self.path
        directory = directory.split('/')

        file_name = directory[len(directory) - 1]
        directory = directory[:len(directory) - 1]
        directory = '/'.join([str(dir) for dir in directory])

        return file_name in os.listdir(directory)

    def save(self, data):
        if self._is_exist():
            self.set_mode('a')

        file = open(self.path, self.mode)

        try:
            file.write(data)
            print("No Error when writing data to disk")
        
        except:
            print("Error When Writing Data to disk")

        finally:
            file.close()