# (generated with --quick)

import okra.models
from typing import Any, Generator, Optional, Type, TypeVar, Union

DataAccessLayer: Type[okra.models.DataAccessLayer]
Inventory: Type[okra.models.Inventory]
Meta: Type[okra.models.Meta]
logger: logging.Logger
logging: module

AnyStr = TypeVar('AnyStr', str, bytes)

def insert_buffer(items, dal, buffer_size = ...) -> None: ...
def parse_inventory(repopath: str, owner: str, project: str) -> Any: ...
def persist_repo(owner: str, project: str, dburl: str, repopath: str, buffer_size: int) -> None: ...
def repo_to_objects(owner: str, project: str, repopath: str, last_commit = ...) -> Generator[Union[okra.models.Author, okra.models.CommitFile, okra.models.Contrib, okra.models.Info, okra.models.Meta], Any, None]: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
