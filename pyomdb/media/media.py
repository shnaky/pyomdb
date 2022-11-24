class Media(object):
    # TODO: add enum for media_t
    def __init__(
        self, title: str, year: int, imdbID: str, media_t: str, poster: str
    ) -> None:
        assert isinstance(title, str), f"source type is {type(title)}"
        assert isinstance(year, int), f"source type is {type(year)}"
        assert isinstance(imdbID, str), f"source type is {type(imdbID)}"
        assert isinstance(media_t, str), f"source type is {type(media_t)}"
        assert isinstance(poster, str), f"source type is {type(poster)}"
        self._title = title
        self._year = year
        self._imdbID = imdbID
        self._media_t = media_t
        self._poster = poster

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
