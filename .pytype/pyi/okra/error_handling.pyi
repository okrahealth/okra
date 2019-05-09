# (generated with --quick)

from typing import Any

class DirectoryNotCreatedError(Error):
    __doc__: str
    expression: Any
    message: Any
    def __init__(self, expression, message) -> None: ...

class Error(Exception):
    __doc__: str

class MissingEnvironmentVariableError(Error):
    __doc__: str
    expression: Any
    message: Any
    def __init__(self, expression, message) -> None: ...

class NetworkError(Error):
    __doc__: str
    expression: Any
    message: Any
    def __init__(self, expression, message) -> None: ...
