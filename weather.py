import settings
from api_connector import APIConnector


class WeatherConnector(APIConnector):
    def __init__(self, data_file, api_url, city_id):
        super().__init__(data_file, api_url)
        self.city_id = city_id
        self._key = None

    @property
    def url(self):
        return self._url.format(
            id=self.city_id, key=self.key)

    @property
    def key(self):
        if not self._key:
            with open(settings.WEATHER_KEY) as f:
                self._key = f.readline().rstrip()
        return self._key


weather_connector = WeatherConnector(
    settings.WEATHER_DATA, settings.WEATHER_URL,
    settings.CITY_ID)
