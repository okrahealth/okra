# (generated with --quick)

from typing import Optional, TypeVar

csv: module
logging: module
os: module
time: module

AnyStr = TypeVar('AnyStr', str, bytes)

def persist_repo(owner: str, project: str, dburl: str, repopath: str, buffer_size: int) -> None: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
