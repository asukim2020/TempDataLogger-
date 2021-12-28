import json
import time
import datetime as dt


class TimeUtil:

    standardHour = 0
    standardMin = 0

    @classmethod
    def getNewTimeByLong(cls):
        return TimeUtil.timeToLong(time.time())

    @classmethod
    def getNewDate(cls):
        t = time.time()
        date = dt.datetime.fromtimestamp(t)
        return date.replace(microsecond=0)

    @classmethod
    def timeToLong(cls, t):
        return int(t * 1000) % 0x10000000000000000

    @classmethod
    def longToDate(cls, t):
        date = TimeUtil.timeToDate(t / 1000)
        return date.replace(microsecond=0)

    @classmethod
    def timeToDate(cls, t):
        return dt.datetime.fromtimestamp(t)

    @classmethod
    def dateToTime(cls, d):
        return d.timestamp()

    @classmethod
    def dateToLong(cls, d):
        t = TimeUtil.dateToTime(d)
        return TimeUtil.timeToLong(t)

    @classmethod
    def getDate(cls, year, month, day):
        dateString = ('%d-%d-%d' % (year, month, day))
        return dt.datetime.strptime(dateString, '%Y-%m-%d')

    @classmethod
    def getNextDay(cls, time, day):
        date = TimeUtil.longToDate(time)
        date += dt.timedelta(days=day)
        return date

    count = 0

    # start of day
    # date = date.replace(hour=0, minute=0, second=0, microsecond=0)

    # end of day
    # date = date.replace(hour=0, minute=0, second=0, microsecond=0)
    # date += datetime.timedelta(days=1, milliseconds=-1)

    @classmethod
    def startOfDay(cls, date):
        return date.replace(hour=0, minute=0, second=0, microsecond=0)

    @classmethod
    def endOfDay(cls, date):
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)
        date += dt.timedelta(days=1, milliseconds=-1)
        return date

    @classmethod
    def checkAMin(cls):
        t = TimeUtil.getNewTimeByLong()
        min = (int)(((t % 3600000) / 60000) % 60)
        return min

    @classmethod
    def checkAClock(cls, hour, maxMin):
        t = TimeUtil.getNewTimeByLong()
        min = ((t % 3600000) / 60000) - TimeUtil.standardMin

        if int((((t % 86400000) / 3600000) + 9 - TimeUtil.standardHour) % 24) % hour == 0\
            and 0 <= min <= maxMin:
            return True
        else:
            return False


# test
if __name__ == "__main__":
    # TimeUtil.checkAMin()
    time = 1639062042063
    print(TimeUtil.longToDate(time))

