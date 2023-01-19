class Rating:
    def __init__(self, Source: str, Value: str) -> None:
        assert isinstance(Source, str), f"source type is {type(Source)}"
        assert isinstance(Value, str), f"value type is {type(Value)}"

        self._source = Source
        self._value = Value

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
