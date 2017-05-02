import settings

import requests

import json
import pickle
import os
from datetime import datetime


class APIConnector:
    def __init__(self, data_file, api_url):
        self.data_file = data_file
        self.url = api_url
        self.info_pattern = '''
It is {description}.
Temperature: {temp} C
wind speed: {speed} m/s
cloudiness: {clouds}%
server was updating: {time}
            '''

    def sync(self):
        response = requests.get(self.url.format(
            id=self.city_id, key=self.__get_key()))
        if response.status_code == 200:
            self.__serialize_data(response.content)
            print('synced')

    def display(self):
        data = self.__load_from_json()
        info = get_info(data)
        print(self.info_pattern.format(**info))

    def __load_from_json(self):
        try:
            size = os.path.getsize(self.data_filename)
        except OSError:
            raise OSError('You should use "sync" method first')
        else:
            data = self.__deserialize_data()
            return json.loads(data)

    def last_sync_time(self):
        try:
            time = os.path.getmtime(self.data_filename)
        except OSError:
            raise OSError('You should use "sync" method first')
        else:
            return time

    def __get_key(self):
        with open(self.key_filename, 'r') as file:
            return file.readline()

    def __serialize_data(self, data):
        with open(self.data_filename, 'wb') as file:
            pickle.dump(data, file)

    def __deserialize_data(self):
        with open(self.data_filename, 'rb') as file:
            return pickle.load(file).decode('utf-8')


def get_info(data):
    description = data['weather'][0]['description']
    temp = data['main']['temp'] / 273.15
    temp = str(round(temp))
    wind_speed = str(data['wind']['speed'])
    clouds = str(data['clouds']['all'])
    time = data['dt']
    time = datetime.fromtimestamp(time).strftime('%d.%m %H:%M')
    return dict(description=description,
                temp=temp, speed=wind_speed,
                clouds=clouds, time=time)


class WeatherConnector(APIConnector):
    def __init__(self):
        super().__init__(settings.WEATHER_DATA,
                         settings.WEATHER_URL)
        self.city_id = settings.CITY_ID
        self.key_file = settings.WEATHER_KEY

    def sync(self):
        pass


class BPConnector(APIConnector):
    pass
