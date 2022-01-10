import serial
import threading

from python.serial.TimeUtil import TimeUtil
from python.serial.WebApi import WebApi as api


class SerialManager:
    port = "/dev/ttyUSB0"
    # port = "COM4"
    baud = 38400
    min = TimeUtil.checkAMin()
    loginCount = 0

    def __init__(self):
        super().__init__()

        # 객체 변수 선언
        self.ser = None
        self.line = []
        self.exitMeasureThread = False
        self.app = None

    def setApp(self, app):
        self.app = app

    def start(self):
        api.login()
        api.getDataLoggerList()
        api.updateDataLogger()

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
                    if self.min < min or (self.min >= 59 and min == 0):
                        self.log(min)

                        tmp = ''.join(self.line)
                        tmp = tmp.replace("+", " , ")
                        tmp = tmp.replace("-", " , -")
                        tmp = tmp.replace("*", "")
                        tmp = tmp.replace("$", "")
                        self.log(tmp)

                        datas = tmp.split(",")

                        dataString = ''
                        firstFlag = False
                        for val in datas:
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

                        count = 4
                        for i in range(0, count):
                            for j in range(0, count):
                                try:
                                    idx = i * count + j + 1
                                    data = float(datas[idx])
                                    data *= 0.1
                                    self.app.children[i].children[j].text = "CH" + str(idx) + ": " + "{:.1f}".format(data)
                                except:
                                    continue

                        self.log(dataString)
                        api.uploadDatas(dataString)

                        self.min = min

                    self.line.clear()

                    SerialManager.loginCount += 1
                    if SerialManager.loginCount >= 1440:
                        api.login()
                        api.updateDataLogger()
                        SerialManager.loginCount = 0

    def end(self):
        self.exitMeasureThread = False

        if self.ser is not None:
            self.ser.write(b"*T$")
            self.ser.close()
            self.ser = None

    def log(self, text):
        try:
            if self.app is not None:
                self.app.children[4].children[0].append(text)
            else:
                print(text)
        except:
            print("log error")
            print(text)


# Test Code
if __name__ == "__main__":
    manager = SerialManager()
    manager.start()
    # manager.end()
