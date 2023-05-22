import requests
import json

class GetAPI:
    def __init__(self):
        self.base_url = 'https://sensus.bps.go.id/topik/tabular/{0}'
        self._set_url = ''

    @property
    def set_url(self):
        return self._set_url

    @set_url.setter
    def set_url(self, value):
        self._set_url = value
        self.url = self.base_url.format(value)

    def getResponse(self, value):
        self.response = requests.get(self.url)
        self.jsonData = json.loads(self.response.content)
        return self.jsonData[value]