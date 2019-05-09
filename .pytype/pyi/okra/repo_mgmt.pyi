# (generated with --quick)

import logging
import okra.error_handling
from typing import Optional, Type, TypeVar

DirectoryNotCreatedError: Type[okra.error_handling.DirectoryNotCreatedError]
NetworkError: Type[okra.error_handling.NetworkError]
logger: logging.Logger
logging: module
os: module
subprocess: module

AnyStr = TypeVar('AnyStr', str, bytes)

def clone_repo(repo_name: str, dirpath: str, ssh = ...) -> bool: ...
def compress_repo(repo_name: str, cache: str, repo_comp: str) -> bool: ...
def create_parent_dir(repo_name: str, dirpath: str) -> bool: ...
def decompress_repo(repo_comp: str, cache) -> bool: ...
def gcloud_clone_or_fetch_repo(repo_name: str, ssh = ...) -> bool: ...
def read_repos(fpath: str) -> list: ...
def update_repo(repo_name: str, dirpath: str) -> bool: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...