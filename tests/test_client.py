import pytest
import pprint


def test_search(client):
    pprint.pprint(str(client.search("titanic")[0]))

    client.search("shrek", type="movie")
    restults = client.search("zoolander", year="1995")
    print(restults[0].__dict__)

def test_by_title(client):
    movie = client.by_title("shrek")
    pprint.pprint(movie.__dict__)
    pprint.pprint(movie.Ratings[0])
    pprint.pprint(movie.Writer)
    movie.Writer = "orestis"
    pprint.pprint(movie.__dict__)


@pytest.mark.parametrize(
    "test_input, expected",
    [({}, True), ({"s": "shrek"}, True), ("invalid", False), (None, False)],
)
def test_set_params(client, test_input, expected):

    params = client._set_params(test_input)
    print("params: ", params)
