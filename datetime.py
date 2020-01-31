import utime as time
import ntptime as ntp


class DateTime:

    def __init__(self, is_connected):
        """
        Constructor ini akan melakukan sync ke ntp server
        Hal ini karena ketika device hard atau softboot
        secara otomatis datetime akan direset menjadi :
        2000-1-1 0:0:0

        :param is_connected: as Boolean
        """
        if is_connected:
            print('Sync to NTP Server')
            ntp.settime()

        else:
            print('Network Not Connected')

    YEAR    = 0
    MONTH   = 1
    DAY     = 2
    HOUR    = 3
    MINUTE  = 4
    SECOND  = 5

    def get_timezone(self):
        """
        Untuk mengambil waktu secara local.
        Device sudah melakukan sync ke ntp server
        namun tidak sesuai dengan timezone Indonesia.
        Untuk itu hasil time.time() menambah dengan 25200

        :return: as List
        """
        _time_ = time.time() + 25200
        return time.localtime(_time_)

    def get_datetime(self):
        """
        Getting Datetime using localtime
        with format : YYYY-MM-DD hh:mm:ss
        and follow index 0 1  2  3  4  5

        :return string
        """
        localtime = self.get_timezone()
        yyyy, mm, dd, h, m, s = localtime[:6]

        return "{}-{}-{} {}:{}:{}".format(
            yyyy, mm, dd,
            h, m, s
        )

    def get_date(self):
        """
        Just untuk mengambil date.

        :return: as String
        """
        localtime = self.get_timezone()
        y, m, d = localtime[:3]

        return "{}-{}-{}".format(y, m, d)

    def get_time(self):
        """
        Just untuk mengambil time.

        :return: as String
        """
        localtime = self.get_timezone()
        h, m, s = localtime[3:6]

        return "{}:{}:{}".format(h, m, s)

    def get(self, arg):
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
        localtime = self.get_timezone()

        return localtime[arg]