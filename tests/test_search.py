from pyomdb.search import Search


def test_init(omdb):
    print(omdb._get_params()["apikey"])
    # print(**omdb._get_params())
    search = Search("shrek", **(omdb._get_params()))

    print(search.title)
    print(search._params)
    assert isinstance(search.title, str)
