from media import Media
from rating import Rating


class MediaInfo(Media):
    def __init__(
        self,
        title,
        year,
        imdbID,
        media_t,
        poster,
        rated,
        released,
        runtime,
        genre,
        director,
        writer,
        actors,
        plot,
        lang,
        ratings,
    ):
        super().__init__(title, year, imdbID, media_t, poster)
        self._rated = rated
        self._released = released
        self._runtime = runtime
        self._genre = genre
        self._director = director
        self._writer = writer
        self._actors = actors
        self._plot = plot
        self._lang = lang
        self._ratings = [Rating]

    @property
    def rated(self):
        return self._rated

    @property
    def released(self):
        return self._released

    @property
    def runtime(self):
        return self._runtime

    @property
    def genre(self):
        return self._genre

    @property
    def director(self):
        return self._director

    @property
    def writer(self):
        return self._writer

    @property
    def actors(self):
        return self._actors

    @property
    def plot(self):
        return self._plot

    @property
    def language(self):
        return self._lang

    @property
    def ratings(self):
        return self._ratings

    @ratings.setter
    def ratings(self, rating_list: list):
        self._ratings = rating_list

    def append_rating(self, rating: Rating):
        self.ratings.append(rating)
