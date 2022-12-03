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
