class Sensor:

    def __init__(self, instance):
        self.instance = instance

    def read_dht(self, date_time=None):
        self.instance.measure()

        humidity = self.instance.humidity()
        temperature = self.instance.temperature()

        data = "humidity:{};\ttemperature:{};\n".format(
            str(humidity), str(temperature))

        if date_time is not None:
            data = "{};\t{}".format(date_time, data)

        return data