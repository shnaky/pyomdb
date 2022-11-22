from omdb import OMDB


class Search(OMDB):
    BASE_PARAM = "s"

    def __init__(self, title, **kwargs):
        super().__init__()
