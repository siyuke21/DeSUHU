import os
import datetime


def get_data(dht, file_name, mode):
    """
    This function used
    to getting and saving data.
    Where needed 3 parameter like:
    :param dht as a Object from DHT11
    :param file_name as String
    :param mode as String is write or append

    :return
    """
    dht.measure()
    humidity = dht.humidity()
    temperature = dht.temperature()
    date_time = datetime.get_datetime()

    file = open(file_name, mode)

    try:
        file.write("{};\thumidity:{};\ttemperature:{};\n".format(
            str(date_time), str(humidity), str(temperature)))

    except:
        println("Error When Writing Data to file")

    finally:
        file.close()