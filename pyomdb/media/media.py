class Media:
    def __init__(self):
        self._title = None
        self._year = None
        self._imdbID = None
        self._type = None
        self._poster = None

    @property
    def title(self):
        return self._title

    @property
    def year(self):
        return self._year

    @property
    def imdbID(self):
        return self._imdbID

    @property
    def type(self):
        return self._type

    @property
    def poster(self):
        return self._poster
