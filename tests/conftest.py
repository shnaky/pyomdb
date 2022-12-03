from pyomdb.omdb import OMDB

import pytest
import os
from os.path import join, dirname, realpath
from dotenv import load_dotenv


@pytest.fixture(scope="session")
def omdb():
    # load .env file to get api key from current dir (/tests/.env)
    dotenv_path = join(dirname(realpath(__file__)), ".env")
    load_dotenv(dotenv_path)
    API_KEY = os.environ.get("OMDB_API_KEY")
    return OMDB(API_KEY)
