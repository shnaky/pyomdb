from pyomdb.client import Client

import pytest
import os
from os.path import join, dirname
from dotenv import load_dotenv

@pytest.fixture(scope="session")
def client():
    # load .env file to get api key from base dir (pyomdb/.env)
    dotenv_path = join(dirname(__file__), "..", ".env")
    load_dotenv(dotenv_path)
    API_KEY = os.environ.get("OMDB_API_KEY")
    return Client(API_KEY)