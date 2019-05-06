# (generated with --quick)

import datetime
import logging
import okra.error_handling
import okra.models
from typing import Any, Generator, Optional, Type, TypeVar, Union

Author: Type[okra.models.Author]
CommitFile: Type[okra.models.CommitFile]
Contrib: Type[okra.models.Contrib]
DirectoryNotCreatedError: Type[okra.error_handling.DirectoryNotCreatedError]
Info: Type[okra.models.Info]
Inventory: Type[okra.models.Inventory]
Meta: Type[okra.models.Meta]
datetime: Type[datetime.datetime]
logger: logging.Logger
logging: module
os: module
re: module

AnyStr = TypeVar('AnyStr', str, bytes)

def make_digit(numstr, desc) -> int: ...
def parse_commits(rpath: str, chash = ...) -> Generator[Any, Any, None]: ...
def parse_committed_files(rpath: str, chash = ...) -> Generator[Any, Any, None]: ...
def parse_messages(rpath: str, chash = ...) -> Generator[Any, Any, None]: ...
def repo_to_objects(repo_name: str, cache: str, last_commit = ...) -> Generator[Union[okra.models.Author, okra.models.CommitFile, okra.models.Contrib, okra.models.Info, okra.models.Meta], Any, None]: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
