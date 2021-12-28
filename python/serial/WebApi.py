import math
import random
import datetime as dt

import requests
import json
from TimeUtil import TimeUtil

class WebApi:
    url = 'http://localhost:8080'
    # url = 'https://mutiscanback.link/'
    companyId = -1
    token = ""
    dataLoggerList = []

    def __init__(self):
        super(WebApi, self).__init__()

    @classmethod
    def signup(cls):
        try:
            user = {
                'name': 'name',
                'loginId': 'test2',
                'loginPw': 'test!'
            }

            response = requests.post(
                cls.url + '/authenticate/signup',
                params=user
            )
            print(response.text)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def login(cls):
        try:
            user = {
                'username': 'test',
                'password': 'test!'
            }

            response = requests.post(
                cls.url + '/authenticate/login',
                json=user
            )
            jstr = response.text
            print(jstr)
            json_data = json.loads(jstr)
            cls.token = json_data['jwtToken']
            cls.companyId = json_data['companyId']

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def createDataLogger(cls):
        try:
            headers = {'Authorization': 'Bearer ' + cls.token}
            response = requests.post(
                cls.url + '/dataLogger/' + str(cls.companyId),
                headers=headers,
                params={'modelName': '데이터로거'}
            )
            print(response.text)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def updateDataLogger(cls):
        try:
            headers = {'Authorization': 'Bearer ' + cls.token}
            param = {
                'id': cls.dataLoggerList[0],
                'modelName': '데이터로거',
                'unit': "uSt, mm, kgf, N, kN, ton, V, g, ', C, cm",
                'channelName': None
            }
            print(json.dumps(param))
            # print(param)
            response = requests.post(
                cls.url + '/dataLogger/update/' + str(cls.companyId),
                headers=headers,
                params=param
            )
            print(response.text)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def getDataLoggerList(cls):
        try:
            headers = {'Authorization': 'Bearer ' + cls.token}
            response = requests.get(
                cls.url + '/dataLogger/' + str(cls.companyId),
                headers=headers
            )
            jstr = response.text
            print(jstr)
            json_data = json.loads(jstr)
            cls.dataLoggerList.clear()
            for data in json_data:
                cls.dataLoggerList.append(data['id'])
                print(data['id'])

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def uploadDatas(cls, data):
        try:
            headers = {'Authorization': 'Bearer ' + cls.token}
            measureDataDtos = []
            # now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
            now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:00.000")[0:23]
            measureDataDtos.append({
                'data': data,
                'time': now
            })
            print(measureDataDtos)
            response = requests.post(
                cls.url + '/measureData/' + str(cls.dataLoggerList[1]),
                headers=headers,
                json=measureDataDtos
            )
            print(response)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def getDatas(cls):
        headers = {'Authorization': 'Bearer ' + cls.token}

        date = dt.datetime.now()
        date += dt.timedelta(days=-1)

        start = TimeUtil.startOfDay(date).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
        end = TimeUtil.endOfDay(date).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]

        query = {
            'from': start,
            'to': end
        }

        dataLoggerId = cls.dataLoggerList[0]

        response = requests.get(
            cls.url + '/measureData/' + str(dataLoggerId),
            headers=headers,
            params=query
        )
        jstr = response.text
        json_data = json.loads(jstr)
        print(json_data)

    @classmethod
    def getDatasAndUpload(cls):
        try:
            headers = {'Authorization': 'Bearer ' + cls.token}

            date = dt.datetime.now()
            date += dt.timedelta(days=-1)

            start = TimeUtil.startOfDay(date).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
            end = TimeUtil.endOfDay(date).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]

            query = {
                'from': start,
                'to': end
            }

            dataLoggerId = cls.dataLoggerList[0]

            response = requests.get(
                cls.url + '/measureData/' + str(dataLoggerId),
                headers=headers,
                params=query
            )
            jstr = response.text
            json_data = json.loads(jstr)
            print(json_data)
            count = int(json_data["count"])
            datas = json_data["data"]
            datas = datas[::-1]
            print(datas)
            addList = []
            if count < 24:
                for i in range(0, count - 1):
                    j = 1
                    while True:
                        date = dt.datetime.strptime(datas[i]["time"], "%Y-%m-%dT%H:%M:%S.%f")
                        time = int(date.timestamp()) + (3600 * j)
                        nextDate = dt.datetime.strptime(datas[i+1]["time"], "%Y-%m-%dT%H:%M:%S.%f")
                        nextTime = int(nextDate.timestamp())
                        if nextTime == time:
                            break
                        else:
                            j += 1
                            t = dt.datetime.fromtimestamp(time).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
                            addList.append({
                                'data': datas[i]["data"],
                                'time': t
                            })

                end = TimeUtil.endOfDay(date).timestamp()
                time = dt.datetime.strptime(datas[count-1]["time"], "%Y-%m-%dT%H:%M:%S.%f").timestamp()

                while True:
                    j = 1
                    time += 3600 * j
                    if end < time:
                        break
                    else:
                        j += 1
                        t = dt.datetime.fromtimestamp(time).strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
                        addList.append({
                            'data': datas[count-1]["data"],
                            'time': t
                        })

                print(addList)
                response = requests.post(
                    cls.url + '/measureData/' + str(dataLoggerId),
                    headers=headers,
                    json=addList
                )
                print(response.text)

            # for data in json_data["data"]:
            #     date = dt.datetime.strptime(data["time"], "%Y-%m-%dT%H:%M:%S.%f")
            #     time = int(date.timestamp())
            #     print(data["data"], time)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)

    @classmethod
    def uploadDatas(cls, dataLoggerId):
        try:
            headers = {'Authorization': 'Bearer ' + cls.token}
            measureDataDtos = []
            datas = []
            now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
            for i in range(0, 3):
                data = str(int(random.random() * 30))
                datas.append(data)
            dataString = ','.join(datas)
            print(dataString)

            measureDataDtos.append({
                'data': dataString,
                'time': now
            })
            print(measureDataDtos)
            response = requests.post(
                cls.url + '/measureData/' + str(dataLoggerId),
                headers=headers,
                json=measureDataDtos
            )
            print(response)

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)


if __name__ == "__main__":
    from WebApi import WebApi as api

    api.login()
    api.getDataLoggerList()
    # api.updateDataLogger()

    api.uploadDatas(31.1)

    # api.getDatas()
    # api.getDatasAndUpload()
    # for dataLoggerId in api.dataLoggerList:
    #     api.uploadDatas(dataLoggerId)

    # api.signup()
    # api.login()
    # api.createDataLogger()