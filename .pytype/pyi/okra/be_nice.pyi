# (generated with --quick)

from typing import Optional, TypeVar

csv: module
logger: logging.Logger
logging: module
os: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

def batch_upsert_repos(batch: list, buffer_size: int, sleep: int, ecount_max = ...) -> None: ...
def clone_or_fetch_repo(repo_path, repo_url) -> bool: ...
def persist_repo(owner: str, project: str, dburl: str, repopath: str, buffer_size: int) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
