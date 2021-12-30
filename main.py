from python.serial.SerialManager import SerialManager
from guizero import App

if __name__ == "__main__":
    import sys
    sys.path.append("/home/pi/Documents/TempDataLogger-")
    sys.path.append("/home/pi/Documents/TempDataLogger-/python/serial")

    # serial = SerialManager()
    # serial.start()

    app = App(title="Hello world")
    app.display()