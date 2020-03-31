import os


def get_data(date_time, dht, file_name, mode):
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

    file = open(file_name, mode)

    try:
        data_write = "{};\thumidity:{};\ttemperature:{};\n".format(
            str(date_time), str(humidity), str(temperature))

        file.write(data_write)
        print(data_write)

    except:
        print("Error When Writing Data to file")

    finally:
        file.close()
        print('Done')