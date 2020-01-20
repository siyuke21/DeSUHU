import utime as time


YEAR    = 0
MONTH   = 1
DAY     = 2
HOUR    = 3
MINUTE  = 4
SECOND  = 5


def get_datetime():
    """
    Getting Datetime using localtime
    with format : YYYY-MM-DD hh:mm:ss

    :return string
    """
    localtime = time.localtime()
    date_time = ""

    for index, value in enumerate(localtime):
        if index < 2:
            # Save Year Character
            date_time += "{}-".format(value)

        elif index == 2:
            # Save Month and Day Character
            date_time += "{} ".format(value)

        elif 2 < index < 5:
            # Save Hour and Minute Character
            date_time += "{}:".format(value)

        elif index == 5:
            # Save Second Character
            date_time += "{}".format(value)

    return date_time


def get(arg):
    """
    :arg: Integer
    Where this argument is :
        0 -> Year
        1 -> Month
        2 -> Day
        3 -> Hour
        4 -> Minute
        5 -> Second

    :return:
    """
    localtime = time.localtime()

    return localtime[arg]