class Rating:
    def __init__(self, source: str, value: str) -> None:
        assert isinstance(source, str), f"source type is {type(source)}"
        assert isinstance(value, str), f"value type is {type(value)}"

        self._source = source
        self._value = value

    @property
    def source(self) -> str:
        return self._source

    @property
    def value(self) -> str:
        return self._value

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}({self._source!r}, {self._value!r})"""

    def __str__(self) -> str:
        return f"""
    source: {self._source}
    value: {self._value}
        """
