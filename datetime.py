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
    and follow index 0 1  2  3  4  5

    :return string
    """
    localtime = time.localtime()
    yyyy, mm, dd, h, m, s = localtime[:6]

    return "{}-{}-{} {}:{}:{}".format(
        yyyy, mm, dd,
        h, m, s
    )


def get_date():
    localtime = time.localtime()
    y, m, d = localtime[:3]

    return "{}-{}-{}".format(y, m, d)


def get_time():
    localtime = time.localtime()
    h, m, s = localtime[3:6]

    return "{}:{}:{}".format(h, m, s)


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