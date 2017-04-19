import json, pickle, os

import requests


class Weather:
    def __init__(self, city_id='706483', key_file='.api.key',
                 data_file='.weather.info'):
        self.city_id = city_id
        self.key_filename = key_file
        self.data_filename = data_file
        self.url = ('http://api.openweathermap.org/'
                    'data/2.5/weather?id={id}&appid={key}')
        self.info_pattern = '''
            It is {description}.
            Temperature: {temp}C
            speed of wind: {speed}
            clouds: {clouds}%
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

    def __last_sync_time(self):
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
    return dict(description=description,
                temp=temp, speed=wind_speed,
                clouds=clouds)