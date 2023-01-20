from pyomdb.media.media import Media
from pyomdb.media.rating import Rating


class MediaInfo(Media):
    # **kwargs for unknown attributs in class (use with set attr)
    def __init__(self, Title, Year, imdbID, Type, Poster, **kwargs):
        print("title: ", Title)
        print(kwargs)
        self._as_json = kwargs
        self.__dict__.update(kwargs)
        super().__init__(Title, Year, imdbID, Type, Poster)
        # Ratings list attribute with Rating instances 
        if kwargs["Ratings"]:
            self.Ratings = [Rating(**x) for x in kwargs["Ratings"]]

    def as_json(self):
        return self._as_json

    def __repr__(self):
        return super().__repr__().join(f"{key}= {value}" for key, value in self.__dict__)
        
    
