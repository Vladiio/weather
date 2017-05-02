import os


BASE_DIR = os.path.abspath('.')

# weather
CITY_ID = '706483'

WEATHER_KEY = os.path.join(BASE_DIR, '.api.key')
WEATHER_DATA = os.path.join(BASE_DIR, '.weather.info')
WEATHER_URL = ('http://api.openweathermap.org/'
               'data/2.5/weather?id={id}&appid={key}')

# currency
PB_DATA = os.path.joins(BASE_DIR, '.currency.info')
PB_URL = ('https://api.privatbank.ua/p24api/pubinfo?'
          'json&exchange&coursid=5')
