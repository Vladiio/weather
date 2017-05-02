import settings
from api_connector import APIConnector


class PBConnector(APIConnector):

    @property
    def url(self):
        return self._url


pb_connector = PBConnector(
    settings.PB_DATA, settings.PB_URL)
