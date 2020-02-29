# (generated with --quick)

import okra.error_handling
from typing import Optional, Type, TypeVar

DirectoryNotCreatedError: Type[okra.error_handling.DirectoryNotCreatedError]
NetworkError: Type[okra.error_handling.NetworkError]
logger: logging.Logger
logging: module
os: module
subprocess: module

AnyStr = TypeVar('AnyStr', str, bytes)

def clone_or_fetch_repo(repo_path, repo_url) -> bool: ...
def clone_repo(repo_url, repo_path) -> bool: ...
def compress_repo(repo_name: str, cache: str, repo_comp: str) -> bool: ...
def decompress_repo(repo_comp: str, cache) -> bool: ...
def update_repo(repopath) -> bool: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
