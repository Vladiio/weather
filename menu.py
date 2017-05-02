#! /usr/bin/env python

import sys
from datetime import datetime

from weather import weather_connector
from exchange import pb_connector


class Menu:

    def __init__(self):
        self.choices = {
            '1': weather_connector.sync,
            '2': self.display_weather,
            '3': self.sync_time,
            '4': pb_connector.sync,
            '5': self.display_exchange,
            '6': self.quit,
        }

    def run(self):
        while True:
            print('''
1. sync weather data with server
2. display last synced weather data
3. last sync time
4. sync exchange rates with server
5. display exchange rates
6. quit
''')
            choice = input('Your choice: ')
            action = self.choices.get(choice)
            if action:
                action()

    def display_weather(self):
        try:
            data = weather_connector.data
        except FileNotFoundError:
            print('You must sync data with server')
        else:
            print('''
It is {}.
Temperature: {} C
wind speed: {} m/s
cloudiness: {}%
                '''.format(data['weather'][0]['description'],
                           data['main']['temp'], data['wind']['speed'],
                           data['clouds']['all']))

    def display_exchange(self):
        try:
            data = pb_connector.data
        except FileNotFoundError:
            print('You must sync data with server')
        else:
            print('''
\tcurrency\tbuy\tsale
\tUSD       \t{}\t{}
                    '''.format(data[2]['buy'], data[2]['sale']))

    def sync_time(self):
        try:
            time = weather_connector.last_sync_time
        except FileNotFoundError:
            print('You must sync data with server')
        else:
            time = datetime.fromtimestamp(
                time).strftime('%d.%m %H:%M')
            print(time)

    def quit(self):
        sys.exit(1)


if __name__ == '__main__':
    Menu().run()
