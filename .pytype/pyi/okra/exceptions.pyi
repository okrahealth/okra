# (generated with --quick)

from typing import Any

class OkraError(Exception):
    __doc__: str

class UrlJoinError(OkraError):
    __doc__: str
    expression: Any
    message: Any
    def __init__(self, expression, message) -> None: ...
