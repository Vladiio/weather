import json

import requests


class Weather:
	def __init__(self):
		self.url = ('http://samples.openweathermap.org/'
				   'data/2.5/weather?id={id}&appid={key}')
		self.city_id = '706483'


	def show(self):
		response = requests.get(self.url.format(
				id=self.city_id, key=self.key))
		print(response.status_code)
