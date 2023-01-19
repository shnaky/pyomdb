from pyomdb.media.media import Media
from pyomdb.media.media_info import MediaInfo

import requests


class ApiKeyError(Exception):
    """
    Raised when there is something wrong with the Api Key
    """
    pass


class Client:
    BASE_URL = "http://www.omdbapi.com"
    HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}

    def __init__(self, api_key):
        assert isinstance(api_key, str)
        self._api_key = api_key
        self._params = {"apikey": self._api_key}

    def search(self, title: str, **kwargs) -> list[Media]:
        """
        Search for OMDB for the given title
            required: title of media
            optional: allowed parameters that the OMDB-API accepts

            return: list of the search results
        """
        search_results = []

        kwargs.update({"s": title})
        params = self._set_params(kwargs)
        response = self._get_request(params)
        for result in response["Search"]:
            search_results.append(Media(**result))
        return search_results

    def by_id(self, id: int, **kwargs) -> MediaInfo:
        kwargs.update({"i": id})
        params = self._set_params(kwargs)
        response = self._get_request(params)
        return MediaInfo(**response)

    def by_title(self, title: str, **kwargs) -> MediaInfo:
        kwargs.update({"t": title})
        params = self._set_params(kwargs)
        response = self._get_request(params)
        return MediaInfo(**response)

    def _set_params(self, params: dict) -> dict:
        """
        Adds the API-Key into the parameter dictionary for the URL API request
        """
        api_dict = {"apikey": self._api_key}
        if isinstance(params, dict):
            params.update(api_dict)
        else:
            params = api_dict
        self._params = params
        return self._params

    def _get_request(self, params: dict) -> dict:
        """ 
        Makes an http-get request with the given arguments
        """
        response = requests.get(url=self.BASE_URL, params=params, headers=self.HEADERS)
        return response.json()

    @property
    def api_key(self):
        return self._api_key

    @property
    def params(self):
        return self._params
