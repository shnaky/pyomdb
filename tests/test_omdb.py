from omdb.omdb import OMDB

import pytest  # use pytest -s for console prints (for debugging)
import os
from os.path import join, dirname, realpath
from dotenv import load_dotenv


# load .env file to get api key from current dir (/tests/.env)
dotenv_path = join(dirname(realpath(__file__)), ".env")
load_dotenv(dotenv_path)
API_KEY = os.environ.get("OMDB_API_KEY")


@pytest.fixture
def omdb():
    return OMDB(API_KEY)


def test_omdb_init(omdb):
    print(omdb.api_key)
    assert isinstance(omdb.api_key, str)


def test_get_params(omdb):
    params = omdb._get_params()
    print(params)
    assert isinstance(params, dict)


def test_get(omdb):
    params = omdb._get("{}").json()
    print(params)
    assert isinstance(params, dict)
