import random
import datetime as dt

import requests
import json

class WebApi:
    # url = 'http://172.30.1.102:8080'
    url = 'https://mutiscanback.link'
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
            print("jstr: ", end=" ")
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
                params={'modelName': '???????????????'}
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
            ip = requests.get('https://api.ipify.org')
            headers = {'Authorization': 'Bearer ' + cls.token}
            param = {
                'id': cls.dataLoggerList[1],
                'modelName': None,
                'unit': None,
                'channelName': None,
                'ip': ip.text
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
    def select(cls):
        from python.serial.TimeUtil import TimeUtil as tu

        try:
            headers = {'Authorization': 'Bearer ' + cls.token}
            offset = dt.datetime.now()
            print(offset)
            start = tu.getNextDay(offset, -60).strftime("%Y-%m-%dT%H:%M:00.000")[0:23]
            end = offset.strftime("%Y-%m-%dT%H:%M:00.000")[0:23]

            param = {
                'from': start,
                'to': end,
                'offset': 300,
            }

            print(param)

            response = requests.get(
                cls.url + '/measureData/download/' + str(cls.dataLoggerList[1]),
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

    # @classmethod
    # def uploadDatas(cls, dataLoggerId):
    #     try:
    #         headers = {'Authorization': 'Bearer ' + cls.token}
    #         measureDataDtos = []
    #         datas = []
    #         now = dt.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[0:23]
    #         for i in range(0, 3):
    #             data = str(int(random.random() * 30))
    #             datas.append(data)
    #         dataString = ','.join(datas)
    #         print(dataString)
    #
    #         measureDataDtos.append({
    #             'data': dataString,
    #             'time': now
    #         })
    #         print(measureDataDtos)
    #         response = requests.post(
    #             cls.url + '/measureData/' + str(dataLoggerId),
    #             headers=headers,
    #             json=measureDataDtos
    #         )
    #         print(response)
    #
    #     except requests.exceptions.HTTPError as errh:
    #         print(errh)
    #     except requests.exceptions.ConnectionError as errc:
    #         print(errc)
    #     except requests.exceptions.Timeout as errt:
    #         print(errt)
    #     except requests.exceptions.RequestException as err:
    #         print(err)


if __name__ == "__main__":
    from WebApi import WebApi as api

    api.login()
    api.getDataLoggerList()
    api.select()
    # api.updateDataLogger()

    # api.uploadDatas(31.1)

    # api.getDatas()
    # api.getDatasAndUpload()
    # for dataLoggerId in api.dataLoggerList:
    #     api.uploadDatas(dataLoggerId)

    # api.signup()
    # api.login()
    # api.createDataLogger()