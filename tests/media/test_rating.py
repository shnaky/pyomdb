from pyomdb.media.rating import Rating
import pytest

rating = Rating("metascore", "99/100")


@pytest.mark.parametrize(
    "source, value", [("RT", 23), (23, "MS"), (3.2, 43), ("RT", "32")]
)
# just a placeholder should be removed
def test_init(source, value):
    if not (isinstance(source, str) and isinstance(value, str)):
        with pytest.raises(AssertionError):
            Rating(source, value)


def test_str():
    print(rating)
    assert isinstance(rating.__str__(), str)


def test_repr():
    print(repr(rating))
    assert isinstance(rating.__repr__(), str)
