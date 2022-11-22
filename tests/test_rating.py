from omdb.media.rating import Rating

rating = Rating("metascore", "99/100")
rating2 = Rating("RottenTomatoes", 23)


def test_str():
    print(rating)
    assert isinstance(rating.__str__(), str)


def test_repr():
    print(repr(rating))
    assert isinstance(rating.__repr__(), str)
