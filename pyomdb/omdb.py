import requests


class OMDB(object):
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    params = {}

    def __init__(self, api_key):
        self._api_key = api_key
        self._url = "http://www.omdbapi.com"

    def _get(self, params):
        params = self._get_params()
        response = requests.get(self._url, params)
        return response

    def _get_params(self):
        params = self.params
        api_dict = {"apikey": self._api_key}
        if params and isinstance(params, dict):
            params.update(api_dict)
        else:
            params = api_dict
        return params

    @property
    def url(self):
        return self._url

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, api_key):
        self._api_key = api_key
