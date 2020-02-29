# (generated with --quick)

import okra.error_handling
from typing import Any, Optional, Type, TypeVar

DirectoryNotCreatedError: Type[okra.error_handling.DirectoryNotCreatedError]
MissingEnvironmentVariableError: Type[okra.error_handling.MissingEnvironmentVariableError]
NetworkError: Type[okra.error_handling.NetworkError]
csv: module
local_persistance: Any
logging: module
os: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

def create_parent_dir(repo_name: str, dirpath: str) -> bool: ...
def gcloud_clone_or_fetch_repo(repo_name: str, ssh = ...) -> bool: ...
def persist_repo(owner: str, project: str, dburl: str, repopath: str, buffer_size: int) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
