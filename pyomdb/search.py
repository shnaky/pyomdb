from pyomdb.omdb import OMDB


class Search(OMDB):
    REQUIRED_PARAM = "s"
    OPTIONAL_PARAM = {
        "type": ["movie, series, episode"],
        "y": int,
        "r": ["json", "xml"],
        "page": {"min_value": 1, "max_value": 100},
        "callback": None,
        "v": None,
    }

    def __init__(self, title, **kwargs):
        print(kwargs["apikey"])
        self._title = title
        self._params = kwargs
        self._params[self.REQUIRED_PARAM] = self._title
        print(self._params)
        self.__dict__.update(kwargs)

    @property
    def title(self):
        return self._title

    def __repr__(self):
        return self.__dict__.copy()
