import serial
import threading

from python.serial.TimeUtil import TimeUtil
from python.serial.WebApi import WebApi as api

class SerialManager:
    port = "/dev/ttyUSB0"
    # port = "COM4"
    baud = 38400
    min = TimeUtil.checkAMin()

    def __init__(self):
        super().__init__()

        # 객체 변수 선언
        self.ser = None
        self.line = []
        self.exitMeasureThread = False

    def start(self):
        api.login()
        api.getDataLoggerList()

        self.exitMeasureThread = True

        if self.ser is None:
            self.ser = serial.Serial(SerialManager.port, SerialManager.baud, timeout=0)
            self.ser.write(b"*S$")

            thread = threading.Thread(target=self.readThread)
            thread.start()

    def readThread(self):
        while self.exitMeasureThread:
            for c in self.ser.read():
                self.line.append(chr(c))

                if c == 10:
                    min = TimeUtil.checkAMin()
                    if self.min < min or (self.min == 59 and min == 0):
                        print(min)

                        tmp = ''.join(self.line)
                        tmp = tmp.replace("+", " , ")
                        tmp = tmp.replace("-", " , -")
                        tmp = tmp.replace("*", "")
                        tmp = tmp.replace("$", "")
                        print(tmp)

                        datas = tmp.split()

                        dataString = ''
                        firstFlag = False
                        for idx, val in enumerate(datas):
                            try:
                                data = float(val)
                                data *= 0.1

                                if firstFlag:
                                   dataString += ','

                                dataString += "{:.1f}".format(data)

                                if not firstFlag:
                                    firstFlag = True

                            except:
                                continue

                        print(dataString)
                        api.uploadDatas(dataString)

                        self.min = min

                    self.line.clear()

    def end(self):
        self.exitMeasureThread = False

        if self.ser is not None:
            self.ser.write(b"*T$")
            self.ser.close()
            self.ser = None


# Test Code
if __name__ == "__main__":
    manager = SerialManager()
    manager.start()
    # manager.end()