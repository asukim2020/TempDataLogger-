from python.serial.SerialManager import SerialManager
from python.serial.WebApi import WebApi as api

if __name__ == "__main__":
    import sys
    sys.path.append("/home/pi/Documents/TempDataLogger-")
    sys.path.append("/home/pi/Documents/TempDataLogger-/python/serial")

    api.login()
    api.getDataLoggerList()

    serial = SerialManager()
    serial.start()