from pyomdb.media.media import Media

import pprint

media = Media("shrek", "2001", "tt0126029", "movie", "poster-link")

def test_as_json():
    json_data = media.as_json()
    pprint.pprint(json_data)

def test_repr():
    print(repr(media))

def test_str():
    print(str(media))