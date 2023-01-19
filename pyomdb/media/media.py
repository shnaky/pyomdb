class Media():
    def __init__(
        self, Title: str, Year: str, imdbID: str, Type: str, Poster: str
    ) -> None:
        assert isinstance(Title, str), f"source type is {type(Title)}"
        assert isinstance(Year, str), f"sour ce type is {type(Year)}"
        assert isinstance(imdbID, str), f"source type is {type(imdbID)}"
        assert isinstance(Type, str), f"source type is {type(Type)}"
        assert isinstance(Poster, str), f"source type is {type(Poster)}"
        self.Title = Title
        self.Year = Year
        self.imdbID = imdbID
        self.Type = Type
        self.Poster = Poster

    def __repr__(self):
        return f"""{self.__class__.__name__}(
            {self.Title
!r}, 
            {self.Year!r}, 
            {self.imdbID!r}, 
            {self.Type!r}, 
            {self.Poster!r}
            )"""

    def __str__(self):
        return f"""
        Title: {self.Title}
        Year: {self.Year}
        ImdbID: {self.imdbID}
        Type: {self.Type}
        Poster: {self.Poster}
        """