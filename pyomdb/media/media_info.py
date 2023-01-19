from pyomdb.media.media import Media
from pyomdb.media.rating import Rating


class MediaInfo(Media):
    # **kwargs for unknown attributs in class (use with set attr)
    def __init__(self, Title, Year, imdbID, Type, Poster, **kwargs):
        print("title: ", Title)
        self.__dict__.update(kwargs)
        super().__init__(Title, Year, imdbID, Type, Poster)
        self.Ratings = [Rating(**x) for x in kwargs["Ratings"]]

    def __repr__(self):
        return super().__repr__().join(f"{key}= {value}" for key, value in self.__dict__)
        
    
