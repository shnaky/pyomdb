class Rating(object):
    def __init__(self, source: str, value: str) -> None:
        assert isinstance(source, str)
        assert isinstance(value, str)
        self._source = source
        self._value = value

    @property
    def source(self) -> str:
        return self._source

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}("{self._source}", "{self._value}")"""

    def __str__(self) -> str:
        return f"""
    source: {self._source}
    value: {self._value}
        """
