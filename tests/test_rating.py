from pyomdb.media.rating import Rating
import pytest

rating = Rating("metascore", "99/100")


def test_init():
    with pytest.raises(AssertionError):
        Rating("RottenTomatoes", 23)


def test_str():
    print(rating)
    assert isinstance(rating.__str__(), str)


def test_repr():
    print(repr(rating))
    assert isinstance(rating.__repr__(), str)
