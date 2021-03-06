# (generated with --quick)

import okra.error_handling
import okra.models
from typing import Any, List, Optional, Tuple, Type, TypeVar

DataAccessLayer: Type[okra.models.DataAccessLayer]
DirectoryNotCreatedError: Type[okra.error_handling.DirectoryNotCreatedError]
MissingEnvironmentVariableError: Type[okra.error_handling.MissingEnvironmentVariableError]
NetworkError: Type[okra.error_handling.NetworkError]
logger: logging.Logger
logging: module
os: module
populate_db: Any
shutil: module

AnyStr = TypeVar('AnyStr', str, bytes)

def clone_repo(repo_name: str, dirpath: str, ssh = ...) -> bool: ...
def compress_repo(repo_name: str, cache: str, repo_comp: str) -> bool: ...
def create_parent_dir(repo_name: str, dirpath: str) -> bool: ...
def decompress_repo(repo_comp: str, cache) -> bool: ...
def get_truck_factor_by_project(owner, project, dal) -> Tuple[int, List[Tuple[Any, Any]]]: ...
def local_persistance(repo_name: str, parent_dir: str, buffer_size = ...) -> None: ...
def retrieve_or_clone(repo_name: str, dirpath: str) -> bool: ...
def update_repo(repo_name: str, dirpath: str) -> bool: ...
def urljoin(base: AnyStr, url: Optional[AnyStr], allow_fragments: bool = ...) -> AnyStr: ...
