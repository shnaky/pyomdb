from pyomdb.media.media_info import MediaInfo

from os.path import join, dirname
import json

# TODO: add all the loading of the resources/media/test_data.json in the media/conftest.py as a fixture
# TODO: add more test data for media_info.py and the other media files.

# Load the test_data from the .json file 
test_data_path = join(dirname(__file__), "..", "resources", "media", "test_data_media_info.json")
test_data = json.load(open(test_data_path, "r"))

# create MediaInfo instance with the loaded test data
media_info = MediaInfo(**test_data)


def test_as_json():
    json_data = media_info.as_json()
    assert isinstance(json_data, dict)
