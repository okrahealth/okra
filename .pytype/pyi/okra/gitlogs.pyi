# (generated with --quick)

from typing import Any, Generator

Commit: Any
File: Any
Inventory: Any
Message: Any
csv: module
logger: logging.Logger
logging: module
os: module
subprocess: module

def parse_commits(rpath: str, chash = ...) -> Generator[Any, Any, None]: ...
def parse_committed_files(rpath: str, chash = ...) -> Generator[Any, Any, None]: ...
def parse_inventory(repopath: str, owner: str, project: str) -> Any: ...
def parse_messages(rpath: str, chash = ...) -> Generator[Any, Any, None]: ...
def write_line_commits(parsed_commits) -> Generator[list, Any, None]: ...
def write_line_messages(parsed_messages) -> Generator[list, Any, None]: ...
