# (generated with --quick)

import logging
import okra.models
from typing import Any, Generator, Optional, Type, TypeVar, Union

DataAccessLayer: Type[okra.models.DataAccessLayer]
Inventory: Type[okra.models.Inventory]
Meta: Type[okra.models.Meta]
logger: logging.Logger
logging: module

AnyStr = TypeVar('AnyStr', str, bytes)

def insert_buffer(items, dal, buffer_size = ...) -> None: ...
def parse_inventory(rpath: str, repo_name: str) -> Any: ...
def populate_db(dburl: str, cache: str, repo_name: str, buffer_size = ...) -> None: ...
def repo_to_objects(repo_name: str, cache: str, last_commit = ...) -> Generator[Union[okra.models.Author, okra.models.CommitFile, okra.models.Contrib, okra.models.Info, okra.models.Meta], Any, None]: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
