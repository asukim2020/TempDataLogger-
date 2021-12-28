import random
import datetime as dt

import requests
import json

class WebApi:
    # url = 'http://localhost:8080'
    url = 'https://mutiscanback.link/'
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
            # json_data = json.loads(jstr)
            # cls.token = json_data['jwtToken']
            # cls.companyId = json_data['companyId']

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