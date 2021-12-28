from python.serial.SerialManager import SerialManager

if __name__ == "__main__":
    import sys
    sys.path.append("/home/pi/Documents/TempDataLogger/python/serial")
    serial = SerialManager()
    serial.start()