import requests

import json
import pickle
import os
from datetime import datetime
import abc


class APIConnector(metaclass=abc.ABCMeta):
    def __init__(self, data_file, api_url):
        self.data_file = data_file
        self._url = api_url
        self._data = None

    @abc.abstractproperty
    def url(self):
        pass

    def sync(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self._data = json.loads(
                response.content.decode('utf-8'))
            self.__serialize_data()
            print('synced')

    @property
    def data(self):
        if not self._data:
            self.__deserialize_data()
        return self._data

    @property
    def last_sync_time(self):
        return os.path.getmtime(
            self.data_file)

    def __serialize_data(self):
        with open(self.data_file, 'wb') as file:
            pickle.dump(self._data, file)

    def __deserialize_data(self):
        with open(self.data_file, 'rb') as file:
            self._data = pickle.load(file)
