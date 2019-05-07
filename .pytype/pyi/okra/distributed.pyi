# (generated with --quick)

import collections
import datetime
import logging
import multiprocessing.pool
import okra.models
from typing import Any, Callable, Iterable, List, Optional, Tuple, Type

Author: Type[okra.models.Author]
CommitFile: Type[okra.models.CommitFile]
Contrib: Type[okra.models.Contrib]
DataAccessLayer: Type[okra.models.DataAccessLayer]
Info: Type[okra.models.Info]
Meta: Type[okra.models.Meta]
datetime: Type[datetime.datetime]
defaultdict: Type[collections.defaultdict]
logger: logging.Logger
logging: module
np: module
os: module
pd: module
re: module

def Pool(processes: Optional[int] = ..., initializer: Optional[Callable] = ..., initargs: Iterable = ..., maxtasksperchild: Optional[int] = ...) -> multiprocessing.pool.Pool: ...
def consolidate_features_target(cache: str, repo_id: str, report = ...) -> None: ...
def create_features_target(df, k = ...) -> Tuple[Any, Any]: ...
def create_working_table(dal: okra.models.DataAccessLayer) -> Any: ...
def getwork_dbinfo(cache: str) -> List[Tuple[str, str, str]]: ...
def num_authors(df, period: str) -> Any: ...
def num_mentors(df, period: str, subperiod: str, k: int) -> Any: ...
def num_orgs(df, period) -> Any: ...
def run_distributed_pool(n_cores: int, func, work: list) -> list: ...
def write_features_target(dbinfo: tuple, k = ...) -> bool: ...
